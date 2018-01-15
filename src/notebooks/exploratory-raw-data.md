

```python
import json
import pandas as pd
import numpy as np
from datetime import datetime as dt

from helpers import utils
```


```python
with open(utils.get_interim_file('flattened.json'), 'r') as fp:
    data = json.load(fp)
```


```python
df = (
    pd.DataFrame(data.get('properties'))
    .assign(timestamp = lambda x: pd.to_datetime(x.timestamp))
    .assign(firstVisible = lambda x: pd.to_datetime(x.firstVisible))
    .assign(listingUpdated = lambda x: pd.to_datetime(x.listingUpdated))
    .set_index('id')
)
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 164 entries, 63374392 to 40381836
    Data columns (total 19 columns):
    addedReduced           164 non-null object
    address                164 non-null object
    agentName              164 non-null object
    buildVersion           164 non-null object
    currency               164 non-null object
    firstVisible           164 non-null datetime64[ns]
    isAuction              164 non-null bool
    latitude               164 non-null float64
    listingUpdateReason    164 non-null object
    listingUpdated         164 non-null datetime64[ns]
    longitude              164 non-null float64
    numBedrooms            164 non-null int64
    numberOfImages         164 non-null int64
    price                  164 non-null int64
    priceFrequency         164 non-null object
    propertySubType        164 non-null object
    propertyUrl            164 non-null object
    summary                164 non-null object
    timestamp              164 non-null datetime64[ns]
    dtypes: bool(1), datetime64[ns](3), float64(2), int64(3), object(10)
    memory usage: 24.5+ KB



```python
df.currency.unique()
```




    array(['GBP'], dtype=object)




```python
df.isAuction.unique()
```




    array([False], dtype=object)




```python
df.numBedrooms.unique()
```




    array([3, 4, 5])




```python
df.propertySubType.unique()
```




    array(['Terraced', 'Flat', 'Semi-Detached', 'Detached', 'House',
           'End of Terrace', 'Not Specified', 'Semi-Detached Bungalow',
           'House Share', 'Detached Bungalow', 'Apartment', 'Cottage',
           'Maisonette', 'Bungalow', 'Town House', 'Private Halls',
           'Ground Flat'], dtype=object)




```python
df.addedReduced.str.split(' ').str.get(0).unique()
```




    array(['Added', 'Reduced'], dtype=object)




```python
df.listingUpdateReason.unique()
```




    array(['new', 'price_reduced'], dtype=object)




```python
df[df.addedReduced.str.find('Added yesterday') == 0].listingUpdateReason.unique()
```




    array(['new'], dtype=object)




```python
# firstVisible can't be trusted, number of instances where it was first visible after listing update
# unless this means first visible in the search results?
df[df.listingUpdated < df.firstVisible].sample(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>addedReduced</th>
      <th>address</th>
      <th>agentName</th>
      <th>buildVersion</th>
      <th>currency</th>
      <th>firstVisible</th>
      <th>isAuction</th>
      <th>latitude</th>
      <th>listingUpdateReason</th>
      <th>listingUpdated</th>
      <th>longitude</th>
      <th>numBedrooms</th>
      <th>numberOfImages</th>
      <th>price</th>
      <th>priceFrequency</th>
      <th>propertySubType</th>
      <th>propertyUrl</th>
      <th>summary</th>
      <th>timestamp</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>63510337</th>
      <td>Added on 11/12/2017</td>
      <td>Macfarlane Place, Uphall, Broxburn, EH52</td>
      <td>OpenRent, London</td>
      <td>4.29.2.1515686502</td>
      <td>GBP</td>
      <td>2018-01-12 09:04:08</td>
      <td>False</td>
      <td>55.926520</td>
      <td>new</td>
      <td>2017-12-11 09:07:15</td>
      <td>-3.505468</td>
      <td>3</td>
      <td>13</td>
      <td>695</td>
      <td>monthly</td>
      <td>Bungalow</td>
      <td>/property-to-rent/property-63510337.html</td>
      <td>This beautifully presented 3 bedroom property is available to rent immediately. The Landlord has upgraded the property and it is truly offered walk in condition. Downstairs the property comprise... ** Property Reference: 318813 **</td>
      <td>2018-01-13 14:55:46</td>
    </tr>
    <tr>
      <th>69764795</th>
      <td>Added on 30/10/2017</td>
      <td>McAffee Gardens, Armadale, Armadale, EH48</td>
      <td>Castlebrae Sales and Letting Ltd, Bathgate Lettings</td>
      <td>4.29.2.1515686502</td>
      <td>GBP</td>
      <td>2017-10-30 17:26:24</td>
      <td>False</td>
      <td>55.888054</td>
      <td>new</td>
      <td>2017-10-30 16:00:03</td>
      <td>-3.696987</td>
      <td>4</td>
      <td>21</td>
      <td>1050</td>
      <td>monthly</td>
      <td>Detached</td>
      <td>/property-to-rent/property-69764795.html</td>
      <td>Castlebrae - New to market! - Exceptionally well presented large 4 bed detached property, offered FURNISHED, only a few minutes walk from Armadale rail station.</td>
      <td>2018-01-13 14:55:46</td>
    </tr>
    <tr>
      <th>70884773</th>
      <td>Added on 04/01/2018</td>
      <td>25 Kirklands Park Street</td>
      <td>Ballantynes, Edinburgh</td>
      <td>4.29.2.1515686502</td>
      <td>GBP</td>
      <td>2018-01-09 01:22:20</td>
      <td>False</td>
      <td>55.958264</td>
      <td>new</td>
      <td>2018-01-04 01:21:17</td>
      <td>-3.414786</td>
      <td>3</td>
      <td>6</td>
      <td>752</td>
      <td>monthly</td>
      <td>Terraced</td>
      <td>/property-to-rent/property-70884773.html</td>
      <td>A beautifully presented three-bedroom mid terrace Townhouse, located in the sought-after village of Kirkliston.</td>
      <td>2018-01-13 14:55:46</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df.listingUpdateReason == 'price_reduced'].sample(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>addedReduced</th>
      <th>address</th>
      <th>agentName</th>
      <th>buildVersion</th>
      <th>currency</th>
      <th>firstVisible</th>
      <th>isAuction</th>
      <th>latitude</th>
      <th>listingUpdateReason</th>
      <th>listingUpdated</th>
      <th>longitude</th>
      <th>numBedrooms</th>
      <th>numberOfImages</th>
      <th>price</th>
      <th>priceFrequency</th>
      <th>propertySubType</th>
      <th>propertyUrl</th>
      <th>summary</th>
      <th>timestamp</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>70582478</th>
      <td>Reduced on 04/01/2018</td>
      <td>Mosside Drive, Blackburn, Bathgate, EH47</td>
      <td>Your Move , Bathgate Lettings</td>
      <td>4.29.2.1515686502</td>
      <td>GBP</td>
      <td>2017-12-11 16:40:12</td>
      <td>False</td>
      <td>55.878082</td>
      <td>price_reduced</td>
      <td>2018-01-04 12:09:14</td>
      <td>-3.622213</td>
      <td>3</td>
      <td>12</td>
      <td>525</td>
      <td>monthly</td>
      <td>Flat</td>
      <td>/property-to-rent/property-70582478.html</td>
      <td>*** AVAILABLE JANUARY *** 3 bedroom Maisonette located in the village of Blackburn. This property has been finished to a great standard and would make a good family home. Property comprises of bright lounge, modern fitted kitchen with new appliances, 2 double bedrooms and a good sized single a...</td>
      <td>2018-01-13 14:55:46</td>
    </tr>
    <tr>
      <th>50760039</th>
      <td>Reduced on 23/11/2017</td>
      <td>Broomhouse Street South, EDINBURGH, Midlothian, EH11</td>
      <td>Fineholm , Edinburgh - Lettings</td>
      <td>4.29.2.1515686502</td>
      <td>GBP</td>
      <td>2017-09-27 15:28:44</td>
      <td>False</td>
      <td>55.924880</td>
      <td>price_reduced</td>
      <td>2017-11-23 11:35:18</td>
      <td>-3.279890</td>
      <td>4</td>
      <td>9</td>
      <td>1150</td>
      <td>monthly</td>
      <td>House</td>
      <td>/property-to-rent/property-50760039.html</td>
      <td>~ HMO property REFURBISHED to excellent standard, 4 bed mid terrace house in popular established residential area of Edinburgh. HMO COMPLIANT!! ~</td>
      <td>2018-01-13 14:55:46</td>
    </tr>
    <tr>
      <th>70189271</th>
      <td>Reduced on 14/12/2017</td>
      <td>151 Jennie Rennies Road, Dunfermline, Fife, KY11</td>
      <td>Galbraith, Perth - Lettings</td>
      <td>4.29.2.1515686502</td>
      <td>GBP</td>
      <td>2017-11-16 22:37:54</td>
      <td>False</td>
      <td>56.060865</td>
      <td>price_reduced</td>
      <td>2017-12-14 22:38:03</td>
      <td>-3.451771</td>
      <td>3</td>
      <td>10</td>
      <td>675</td>
      <td>monthly</td>
      <td>Not Specified</td>
      <td>/property-to-rent/property-70189271.html</td>
      <td>End terraced property on corner plot. Sitting Room, Dining Kitchen, Utility, 3 bedroom, Shower Room and WC. GCH, DG, driveway. Available furnished from 28/1/18. Restrictions: Pets considered. Council Tax: B. Deposit: &amp;pound;1,350. Landord Reg No: 433081/250/21471. EER: D(57).</td>
      <td>2018-01-13 14:55:46</td>
    </tr>
    <tr>
      <th>68643812</th>
      <td>Reduced on 10/10/2017</td>
      <td>78, Mathieson Place, Dunfermline, Fife, KY11</td>
      <td>Morgans, Dunfermline</td>
      <td>4.29.2.1515686502</td>
      <td>GBP</td>
      <td>2017-09-01 16:34:32</td>
      <td>False</td>
      <td>56.062072</td>
      <td>price_reduced</td>
      <td>2017-10-10 15:33:48</td>
      <td>-3.420788</td>
      <td>3</td>
      <td>10</td>
      <td>650</td>
      <td>monthly</td>
      <td>End of Terrace</td>
      <td>/property-to-rent/property-68643812.html</td>
      <td>Furnished or Unfurnished spacious family home in popular residential area affording accommodation over two levels. Ideally placed for all local amenities and schooling. The subjects briefly comprise entrance hall, lounge/dining area, kitchen with washing machine, fridge/freezer, oven and hob. O...</td>
      <td>2018-01-13 14:55:46</td>
    </tr>
    <tr>
      <th>51749535</th>
      <td>Reduced on 13/12/2017</td>
      <td>Buckstone Loan East, Edinburgh, EH10</td>
      <td>Home Lettings Scotland, Lasswade - Lettings</td>
      <td>4.29.2.1515686502</td>
      <td>GBP</td>
      <td>2017-11-21 16:52:35</td>
      <td>False</td>
      <td>55.907280</td>
      <td>price_reduced</td>
      <td>2017-12-13 16:34:47</td>
      <td>-3.198690</td>
      <td>3</td>
      <td>9</td>
      <td>1190</td>
      <td>monthly</td>
      <td>Semi-Detached</td>
      <td>/property-to-rent/property-51749535.html</td>
      <td>If home is the most satisfying place for you to be, then this 3 bed semi detached property would make an ideal rental.</td>
      <td>2018-01-13 14:55:46</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sample(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>addedReduced</th>
      <th>address</th>
      <th>agentName</th>
      <th>buildVersion</th>
      <th>currency</th>
      <th>firstVisible</th>
      <th>isAuction</th>
      <th>latitude</th>
      <th>listingUpdateReason</th>
      <th>listingUpdated</th>
      <th>longitude</th>
      <th>numBedrooms</th>
      <th>numberOfImages</th>
      <th>price</th>
      <th>priceFrequency</th>
      <th>propertySubType</th>
      <th>propertyUrl</th>
      <th>summary</th>
      <th>timestamp</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>69845429</th>
      <td>Added on 02/11/2017</td>
      <td>Glencoe, Whitburn, Whitburn, EH47</td>
      <td>Castlebrae Sales and Letting Ltd, Bathgate Lettings</td>
      <td>4.29.2.1515686502</td>
      <td>GBP</td>
      <td>2017-11-02 12:02:58</td>
      <td>False</td>
      <td>55.865660</td>
      <td>new</td>
      <td>2017-11-02 12:03:03</td>
      <td>-3.668700</td>
      <td>3</td>
      <td>18</td>
      <td>695</td>
      <td>monthly</td>
      <td>Semi-Detached</td>
      <td>/property-to-rent/property-69845429.html</td>
      <td>CastleBrae - Delightful 3 bed semi detached property, offered part furnished, in popular location</td>
      <td>2018-01-13 14:55:46</td>
    </tr>
    <tr>
      <th>52039749</th>
      <td>Added on 12/12/2017</td>
      <td>East Pilton Farm Crescent, Pilton, Edinburgh, EH5</td>
      <td>Clan Gordon , Edinburgh - Lettings</td>
      <td>4.29.2.1515686502</td>
      <td>GBP</td>
      <td>2017-12-12 20:03:52</td>
      <td>False</td>
      <td>55.972330</td>
      <td>new</td>
      <td>2017-12-12 20:03:57</td>
      <td>-3.226010</td>
      <td>3</td>
      <td>11</td>
      <td>995</td>
      <td>monthly</td>
      <td>Flat</td>
      <td>/property-to-rent/property-52039749.html</td>
      <td>**Available Now** Freshly decorated large and spacious 3 bedroom new build third floor furnished flat (no HMO licence).</td>
      <td>2018-01-13 14:55:46</td>
    </tr>
    <tr>
      <th>63402316</th>
      <td>Added on 04/01/2018</td>
      <td>INVERESK ROAD, MUSSELBURGH, EH21 7BE</td>
      <td>D J Alexander, Edinburgh</td>
      <td>4.29.2.1515686502</td>
      <td>GBP</td>
      <td>2018-01-04 17:04:06</td>
      <td>False</td>
      <td>55.939674</td>
      <td>new</td>
      <td>2018-01-04 17:04:10</td>
      <td>-3.052205</td>
      <td>3</td>
      <td>14</td>
      <td>900</td>
      <td>monthly</td>
      <td>Flat</td>
      <td>/property-to-rent/property-63402316.html</td>
      <td>DEPOSIT &amp;pound;900 - Stylish and beautifully appointed, three bedroom flat within a modern development located in the popular coastal town of Musselburgh, which lies between the city of Edinburgh and East Lothian, AVAILABLE NOW, UNFURNISHED. Musselburgh has an excellent selection of specialist shops, s...</td>
      <td>2018-01-13 14:55:46</td>
    </tr>
    <tr>
      <th>62215459</th>
      <td>Added on 11/10/2017</td>
      <td>Learmonth Crescent, West Calder</td>
      <td>Homes 4 U, Bathgate</td>
      <td>4.29.2.1515686502</td>
      <td>GBP</td>
      <td>2017-10-11 16:49:53</td>
      <td>False</td>
      <td>55.851137</td>
      <td>new</td>
      <td>2017-10-11 16:49:56</td>
      <td>-3.569514</td>
      <td>4</td>
      <td>8</td>
      <td>1000</td>
      <td>monthly</td>
      <td>Cottage</td>
      <td>/property-to-rent/property-62215459.html</td>
      <td>CHARMING VICTORIAN DETACHED COTTAGE located in the heart of West Calder. This spacious, stone built property comprises of vestibule and hallway with beautiful ornate orginal cornacing, high ceilings and cloakroom area. The lounge has traditional solid fuel fire with ornate surround, high ceiling...</td>
      <td>2018-01-13 14:55:46</td>
    </tr>
    <tr>
      <th>51970008</th>
      <td>Added on 07/12/2017</td>
      <td>Learmonth Grove, Comely Bank, City Centre</td>
      <td>Murray &amp; Currie, Edinburgh - Lettings</td>
      <td>4.29.2.1515686502</td>
      <td>GBP</td>
      <td>2017-12-07 09:28:15</td>
      <td>False</td>
      <td>55.957920</td>
      <td>new</td>
      <td>2017-12-07 09:28:18</td>
      <td>-3.221070</td>
      <td>3</td>
      <td>9</td>
      <td>1195</td>
      <td>monthly</td>
      <td>Flat</td>
      <td>/property-to-rent/property-51970008.html</td>
      <td>This three bedroom flat is fully furnished and would suit a professional let. There is no HMO license on the property and not suitable for students.\nThe accommodation has been painted throughout and new carpets added, and comprises of three bedrooms, sitting room, brand new bathroom, modern kitch...</td>
      <td>2018-01-13 14:55:46</td>
    </tr>
  </tbody>
</table>
</div>


