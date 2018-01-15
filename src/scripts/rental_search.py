import requests
import json
import re
import datetime as dt
from bs4 import BeautifulSoup
from time import sleep

from helpers.utils import get_raw_html, get_raw_json, get_logger

logger = get_logger(__name__)


def parse_search_page(search_req):
    logger.info('parsing search page')
    soup = BeautifulSoup(search_req.text, 'html5lib')

    pattern = re.compile(r'window.jsonModel = ', re.DOTALL | re.MULTILINE)
    match = soup.find('script', text=pattern)

    script_content = match.text
    data = json.loads(script_content.replace('window.jsonModel = ',''))

    return (soup, data)


def save_html(req, file_time, page):
    search_html_file = get_raw_html('search-%s-%s.html' % (file_time, page))
    with open(search_html_file, 'wb') as fp:
        fp.write(req.content)
        logger.info('search %s executed: %s saved to disk' % (page, search_html_file))


def save_json(data, file_time, page):
    search_json_file = get_raw_json('search-%s-%s.json' % (file_time, page))
    with open(search_json_file, 'w') as fp:
        # remove indent once happy with script to save on file size
        json.dump(data, fp, sort_keys=True, indent=2)
        logger.info('saving search %s json: %s saved to disk' % (page, search_json_file))


def get_initial_search_results(file_time):
    url = "http://www.rightmove.co.uk/property-to-rent/find.html?searchType=RENT&locationIdentifier=REGION%5E475&insId=2&radius=10.0&minPrice=&maxPrice=1200&minBedrooms=3&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&sortByPriceDescending=&includeLetAgreed=true&_includeLetAgreed=on&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&letType=&letFurnishType=&houseFlatShare=false"
    logger.info('Fetching initial search page')
    r = requests.get(url) # fetch initial search page (index 0, page 0)
    save_html(r, file_time, 1)

    soup, data = parse_search_page(r)
    save_json(data, file_time, 1)

    return data


def get_paged_search_results(file_time, page, index):
    url = "http://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E475&minBedrooms=3&maxPrice=1200&radius=10.0&includeLetAgreed=true"
    url = url + "&index={}".format(index)
    logger.info('Fetching page %s search results (index %s)' % (page, index))
    r = requests.get(url)
    save_html(r, file_time, page)

    soup, data = parse_search_page(r)
    save_json(data, file_time, page)


if __name__ == "__main__":
    search_file_time = dt.datetime.today().strftime('%s')

    initial_data = get_initial_search_results(search_file_time)

    for pager in initial_data.get('pagination').get('options'):
        index = pager.get('value')
        page = pager.get('description')

        if index == '0': continue
        sleep(5)
        get_paged_search_results(search_file_time, page, index)
