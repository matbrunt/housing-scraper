[Swanston Drive, Fairmilehead, Edinburgh](http://www.rightmove.co.uk/property-to-rent/property-52156854.html?utm_content=v2-ealertspropertyimage&utm_medium=email&utm_source=emailupdates&utm_campaign=emailupdatesinstant&utm_term=letting&sc_id=25412504&onetime_FromEmail=true)

```python
import requests

url = "http://www.rightmove.co.uk/property-to-rent/property-52156854.html?utm_content=v2-ealertspropertyimage&utm_medium=email&utm_source=emailupdates&utm_campaign=emailupdatesinstant&utm_term=letting&sc_id=25412504&onetime_FromEmail=true"

r = requests.get(url)

with open('rightmove-test.html', 'wb') as localfile:
    localfile.write(r.content)

# type(r.content) # <class 'bytes'>
# type(r.text) # <class 'str'>
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
soup.select("ul.stations-list > li > span")

import json

# regex: \('branch',(.+)\)\);

>>> json.loads(x)
{'companyName': 'Bondsave Ltd', 'companyType': 'IEA', 'branchName': 'Edinburgh, Lettings', 'pageType': 'Microsite', 'branchId': 71639, 'agentType': 'ea_lettings', 'displayAddress': '92 Morningside Road Edinburgh EH10 4BY ', 'brandName': 'Braemore', 'branchPostcode': None}
>>> json.loads(x).get('brandName')
'Braemore'

import re
m = re.search("\('branch',(.+)\)\);", r.text)
>>> m.group(1)
'{"branchId":71639,"companyName":"Bondsave Ltd","brandName":"Braemore","branchName":"Edinburgh, Lettings","companyType":"IEA","agentType":"ea_lettings","displayAddress":"92 Morningside Road Edinburgh EH10 4BY ","branchPostcode":null,"pageType":"Microsite"}'
>>> json.loads(m.group(1))
{'companyName': 'Bondsave Ltd', 'companyType': 'IEA', 'branchName': 'Edinburgh, Lettings', 'pageType': 'Microsite', 'branchId': 71639, 'agentType': 'ea_lettings', 'displayAddress': '92 Morningside Road Edinburgh EH10 4BY ', 'brandName': 'Braemore', 'branchPostcode': None}
>>> json.loads(m.group(1)).get('brandName')
'Braemore'
```

[BeautifulSoup CSS Selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors)

```python
soup.select("div.sect > p")[0].text


```javascript
<script>
        
    (function(k,v){
      RIGHTMOVE.ANALYTICS.DataLayer.pushKV(k,v);
    }('property',{"location":{"postcode":"EH10 7BL","country":"GB","latitude":55.89778321248135,"longitude":-3.2047894365485763},"propertyId":52156854,"viewType":"Current","imageCount":4,"floorplanCount":0,"videoProvider":"No Video","propertyInfo":{"propertyType":"Flats / Apartments","propertySubType":"Flat","price":1095.0,"beds":3,"added":"20171221","soldSTC":false,"retirement":null,"preOwned":"Resale","ownership":"Non-shared ownership","auctionOnly":false,"letAgreed":false,"lettingType":"Long term","furnishedType":"Furnished","minSizeFt":0,"maxSizeFt":0,"minSizeAc":0.0,"maxSizeAc":0.0,"businessForSale":false,"priceQualifier":"None","currency":"GBP","selectedPrice":null,"selectedCurrency":null}}));
  </script>
    <script>
        
    (function(k,v){
      RIGHTMOVE.ANALYTICS.DataLayer.pushKV(k,v);
    }('branch',{"branchId":71639,"companyName":"Bondsave Ltd","brandName":"Braemore","branchName":"Edinburgh, Lettings","companyType":"IEA","agentType":"ea_lettings","displayAddress":"92 Morningside Road Edinburgh EH10 4BY ","branchPostcode":null,"pageType":"Microsite"}));
  </script>

      propertyId: 52156854,
      propertyPostcode: "EH10 7BL",

images : [{"index":0,"caption":"1","thumbnailUrl":"http://media.rightmove.co.uk/dir/72k/71639/52156854/71639_15065_IMG_01_0000_max_135x100.jpg","masterUrl":"http://media.rightmove.co.uk/dir/72k/71639/52156854/71639_15065_IMG_01_0000_max_656x437.jpg"},{"index":1,"caption":"2","thumbnailUrl":"http://media.rightmove.co.uk/dir/72k/71639/52156854/71639_15065_IMG_02_0000_max_135x100.jpg","masterUrl":"http://media.rightmove.co.uk/dir/72k/71639/52156854/71639_15065_IMG_02_0000_max_656x437.jpg"},{"index":2,"caption":"3","thumbnailUrl":"http://media.rightmove.co.uk/dir/72k/71639/52156854/71639_15065_IMG_03_0000_max_135x100.jpg","masterUrl":"http://media.rightmove.co.uk/dir/72k/71639/52156854/71639_15065_IMG_03_0000_max_656x437.jpg"},{"index":3,"caption":"4","thumbnailUrl":"http://media.rightmove.co.uk/dir/72k/71639/52156854/71639_15065_IMG_04_0000_max_135x100.jpg","masterUrl":"http://media.rightmove.co.uk/dir/72k/71639/52156854/71639_15065_IMG_04_0000_max_656x437.jpg"}]

totalImages : 4,
```

http://www.192.com/schools/search/location?gre=324750&grn=667850&location=EH10+7BL&showOnlySchoolsIcanGetInto=&faith=&grammar=&state=&ofsted1=&ofsted2=&ofsted3=&ofsted4=&withNoOfstedData=

Look at pulling server timestamp to compare pages against each other?

`dataLayer.pushKV('page', {"uri":"/property-to-rent/property-52156854.html","referrer":null,"serverTimestamp":1515501885493,"svr":"2713","channel":"lettings","isEmbedded":false,"ismSitePage":false});`

```html
<meta property="og:description" content="3 bedroom flat to rent in Swanston Drive, Fairmilehead, Edinburgh &pound;1,095 pcm. Marketed by Braemore, Edinburgh, Lettings"/>
<meta property="og:url" content="http://www.rightmove.co.uk/property-to-rent/property-52156854.html"/>

<meta name="twitter:description" content="3 bedroom flat to rent in Swanston Drive, Fairmilehead, Edinburgh &pound;1,095 pcm. Marketed by Braemore, Edinburgh, Lettings">
<meta name="twitter:url" content="http://www.rightmove.co.uk/property-to-rent/property-52156854.html">
```

soup = BeautifulSoup(content, 'html5lib')
pattern = re.compile(r'window.jsonModel = ', re.DOTALL | re.MULTILINE)
match = soup.find('script', text=pattern)
script_content = match.text
data = json.loads(script_content.replace('window.jsonModel = ',''))