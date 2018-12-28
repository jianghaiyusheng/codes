import os
from os import path
import pandas as pd

period=8
period_count=3

sourceDir='temp2'
# targetDir='target'
filenames=os.listdir(sourceDir)
for filename in filenames:
    df=pd.read_csv(path.join(sourceDir,filename),parse_dates=[0],index_col=0,header=None)
    date=df.index[0].date()
    startDt=pd.to_datetime(date)
    print(date,end='\t')
    for i in range(1,period_count):
        prices=df[2][startDt.replace(hour=period*(i-1)):startDt.replace(hour=period*i)]
        print('%.2f'%(prices.max()-prices.min()),end='\t')
    # line1=pd.to_datetime(date).replace(hour=8)
    # line2=pd.to_datetime(date).replace(hour=16)
    # prices1=df[2][:line1]
    # prices2=df[2][line1:line2]
    # prices3=df[2][line1:]
    # print('%s\t%.2f\t%.2f\t%.2f'%(date,prices1.max()-prices1.min(),prices2.max()-prices2.min(),prices3.max()-prices3.min()))
    prices=df[2][startDt.replace(hour=period*(period_count-1)):]
    print('%.2f'%(prices.max()-prices.min()))

