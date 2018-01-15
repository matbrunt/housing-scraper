import re

from helpers.utils import get_external_file, get_interim_file

with open(get_external_file('rightmove-emails.mbox'), 'r') as infile:
  content = infile.read()
  content = content.replace("\n","").replace("=","")

  # http://www.rightmove.co.uk/property-to-rent/property-63171853.html
  urls = set(re.findall("(?P<url>http://www.rightmove.co.uk/property-to-rent/property-\d+.html)", content))
  urls = sorted(urls)

with open(get_interim_file('email-urls.txt'), 'w') as outfile:
  for url in urls:
    outfile.write('%s\n' % url)
