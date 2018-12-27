import os
from os import path
import pandas as pd

sourceDir='target'
targetDir='temp1'
filenames=os.listdir(sourceDir)
for filename in filenames:
	df=pd.read_csv(path.join(sourceDir,filename),parse_dates=[0])
	df.to_csv(path.join(targetDir,filename),index=False,date_format='%Y-%m-%d %H:%M:%S')
