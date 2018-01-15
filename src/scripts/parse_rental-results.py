import json
from datetime import datetime as dt

from helpers.utils import get_logger, get_raw_json, get_interim_file

logger = get_logger(__name__)


def build_search_info(data):
    return {
        'buildVersion': data.get('applicationProperties').get('info.build.version'),
        'isBot': data.get('bot'),
        'deviceType': data.get('deviceType'),
        'listViewUrl': data.get('listViewUrl'),
        'resultPages': data.get('pagination').get('total'),
        'searchDate': parse_timestamp(data.get('recentSearchModel').get('createDate')),
        'resultCount': int(data.get('resultCount')),
        'timestamp': parse_timestamp(data.get('timestamp'))
    }

def build_list_result_info(item, search_info):
    return {
        'buildVersion': search_info['buildVersion'],
        'timestamp': search_info['timestamp'],
        'addedReduced': item.get('addedOrReduced'), # Added on 03/01/2018
        'isAuction': item.get('auction'), # false
        'numBedrooms': item.get('bedrooms'), # 3
        'agentName': item.get('customer').get('branchDisplayName'), # Holburn Property Group, Livingston
        'address': item.get('displayAddress'), # 26, Gladstone Place, Dunfermline, Fife, KY12
        'firstVisible': parse_timestamp(item.get('firstVisibleDate')), # 1514972876000
        'id': item.get('id'), # 63374392
        'listingUpdated': parse_timestamp(item.get('listingUpdate').get('listingUpdateDate')), # 1514972878000
        'listingUpdateReason': item.get('listingUpdate').get('listingUpdateReason'), # new
        'latitude': item.get('location').get('latitude'), # 56.12527
        'longitude': item.get('location').get('longitude'), # -3.18825
        'numberOfImages': item.get('numberOfImages'), # 6
        'price': item.get('price').get('amount'), # 445
        'priceFrequency': item.get('price').get('frequency'), # monthly
        'currency': item.get('price').get('currencyCode'), # GBP
        'propertySubType': item.get('propertySubType'), # Terraced
        'propertyUrl': item.get('propertyUrl'), # /property-to-rent/property-63374392.html
        'summary': item.get('summary')
    }

def parse_timestamp(ts):
    # 1515855346722
    # we need to drop the last 3 digits for the POSIX timestamp
    return dt.fromtimestamp(int(str(ts)[:-3]))

def json_datetime_handler(x):
    if isinstance(x, dt):
        return x.isoformat()
    raise TypeError("Unknown type")


if __name__ == "__main__":
    results = {'searchInfo': None, 'properties': []}

    for page in range(1,8):
        with open(get_raw_json('search-1515855339-%s.json' % page), 'r') as fp:
            data = json.load(fp)

        if page == 1:
            results['searchInfo'] = build_search_info(data)

        properties = [build_list_result_info(item, results['searchInfo']) for item in data.get('properties')]
        results['properties'].extend(properties)

    flattened_file = get_interim_file('flattened.json')
    with open(flattened_file, 'w') as fp:
        json.dump(results, fp, sort_keys=True, indent=2, default=json_datetime_handler)
        logger.info('saving flattened structure to disk: %s' % flattened_file)
