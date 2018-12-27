import os
from os import path
import pandas as pd


sourceDir='temp1'
targetDir='temp2'
filenames=os.listdir(sourceDir)
for filename in filenames:
	df=pd.read_csv(path.join(sourceDir,filename),parse_dates=[0])
	df.groupby(['timestamp','side'])['price'].mean().to_csv(path.join(targetDir,filename))
