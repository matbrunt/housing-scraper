
# coding: utf-8



import json
import pandas as pd
import numpy as np
from datetime import datetime as dt

from helpers import utils




with open(utils.get_interim_file('flattened.json'), 'r') as fp:
    data = json.load(fp)




df = (
    pd.DataFrame(data.get('properties'))
    .assign(timestamp = lambda x: pd.to_datetime(x.timestamp))
    .assign(firstVisible = lambda x: pd.to_datetime(x.firstVisible))
    .assign(listingUpdated = lambda x: pd.to_datetime(x.listingUpdated))
    .set_index('id')
)
df.info()




df.currency.unique()




df.isAuction.unique()




df.numBedrooms.unique()




df.propertySubType.unique()




df.addedReduced.str.split(' ').str.get(0).unique()




df.listingUpdateReason.unique()




df[df.addedReduced.str.find('Added yesterday') == 0].listingUpdateReason.unique()




# firstVisible can't be trusted, number of instances where it was first visible after listing update
# unless this means first visible in the search results?
df[df.listingUpdated < df.firstVisible].sample(3)




df[df.listingUpdateReason == 'price_reduced'].sample(5)




df.sample(5)

