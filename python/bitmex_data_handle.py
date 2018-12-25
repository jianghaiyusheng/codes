import os
from os import path
import pandas as pd
from dateutil.parser import parse

def dt_str_handle(s):
	return s.replace('D',' ')

sourceDir='source'
targetDir='target'
filenames=os.listdir(sourceDir)
for filename in filenames:
	df=pd.read_csv(path.join(sourceDir,filename),converters={'timestamp':dt_str_handle})
	btc_df=df[df.symbol=='XBTUSD']
	simple_df=btc_df.loc[:,['timestamp','side','size','price']]
	simple_df.to_csv(path.join(targetDir,filename),index=False)

'''
def date_parse(s):
	s.replace('D','T')
    dt=parse(s)
	return dt	
df=pd.read_csv(filename,parse_dates=[0],date_parser=date_parse)
'''



