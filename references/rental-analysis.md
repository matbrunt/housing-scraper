# Rental Analysis

## Notes

[sample scraper](https://github.com/woblers/rightmove_webscraper.py/blob/master/rightmove_webscraper.py)

[Scottish Landlord Register](https://www.landlordregistrationscotland.gov.uk/)

[Registers held by "Registers of Scotland"](https://www.ros.gov.uk/about-us/registers-we-hold)

**Search Url**

Search: Edinburgh

Radius: 10 miles

Max Price: £1200 PCM

Min Bedrooms: 3

Include let agreed

Page1: http://www.rightmove.co.uk/property-to-rent/find.html?searchType=RENT&locationIdentifier=REGION%5E475&insId=2&radius=10.0&minPrice=&maxPrice=1200&minBedrooms=3&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&sortByPriceDescending=&includeLetAgreed=true&_includeLetAgreed=on&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&letType=&letFurnishType=&houseFlatShare=false

http://www.rightmove.co.uk/property-to-rent/find.html?
searchType=RENT
locationIdentifier=REGION%5E475
insId=2
radius=10.0
minPrice=
maxPrice=1200
minBedrooms=3
maxBedrooms=
displayPropertyType=
maxDaysSinceAdded=
sortByPriceDescending=
includeLetAgreed=true
_includeLetAgreed=on
primaryDisplayPropertyType=
secondaryDisplayPropertyType=
oldDisplayPropertyType=
oldPrimaryDisplayPropertyType=
letType=
letFurnishType=
houseFlatShare=false

Alternative (when paging back from page 2 to page 1): http://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E475&minBedrooms=3&maxPrice=1200&radius=10.0&includeLetAgreed=true

http://www.rightmove.co.uk/property-to-rent/find.html?
locationIdentifier=REGION%5E475
minBedrooms=3
maxPrice=1200
radius=10.0
includeLetAgreed=true

Page 2: http://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E475&minBedrooms=3&maxPrice=1200&radius=10.0&index=24&includeLetAgreed=true

http://www.rightmove.co.uk/property-to-rent/find.html?
locationIdentifier=REGION%5E475
minBedrooms=3
maxPrice=1200
radius=10.0
index=24
includeLetAgreed=true

Page 3: http://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E475&minBedrooms=3&maxPrice=1200&radius=10.0&index=48&includeLetAgreed=true

http://www.rightmove.co.uk/property-to-rent/find.html?
locationIdentifier=REGION%5E475
minBedrooms=3
maxPrice=1200
radius=10.0
index=48
includeLetAgreed=true

## Search Criteria

- Search Radius

- Price Range

- Num of bedrooms

- Property Types

- Added to site: [Anytime, Last 24 hours, 3 days, 7 days, 14 days]

## Ideas

- Parse html into JSON objects initially, then we can load those objects into a DataFrame.
    - can we set some form of protobuf validation up to verify the JSON objects?
    - add an initial version string to JSON object so we know what the object structure looks like

- Look at how many properties come under the same landlord numbers

- Track number of duplicate entries between searches, this will give us a metric for how often to run the scrapers?

- Add my own version key to RightMove JSON on saving, then can reflect changes to the JSON in future periods
    - would just creating a protobuf have the same impact?

- Track page number a result appears on throughout its history, see if it moves in a particular direction prior to disappearing

## To Do

- parse all json to build up a master list of agents ('branches' in RM)