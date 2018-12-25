import pandas as pd
from dateutil.parser import parse

start_dt='04:00'
end_dt='06:00'
lichas=[0.1,0.2,0.3]
filename='11.7PDCE.csv'

class Algo(object):
    def setStartPoint(self,start_point):
        self.line1=start_point+licha*2
        self.line2=start_point+licha
        self.line3=start_point-licha
        self.line4=start_point-licha*2
        self.first_touched=False
        self.first_touch_line=0
        self.second_touch=False
        # self.cur_flag=Profit #当前盈亏标志
        # self.second_touch_line=0

def date_parse(s):
    dt=parse(s)
    if dt.hour<12 :
        return dt.replace(day=dt.day+1)
    else :
        return dt

df=pd.read_csv(filename,parse_dates=[0],date_parser=date_parse,index_col=0)
price_series=df['成交']
obj_series=price_series[date_parse(start_dt):date_parse(end_dt)]

#获取振幅
scope=obj_series.max()-obj_series.min()
print('振幅：%.2f'%scope)

algo=Algo()
for licha in lichas:
    profit,loss=0,0
    algo.setStartPoint(obj_series[0])
    for i in range(1,len(obj_series)):
        v=obj_series[i]
        if not algo.first_touched:
            if v>=algo.line2:
                algo.first_touched=True
                algo.first_touch_line=2
            elif v<=algo.line3:
                algo.first_touched=True
                algo.first_touch_line=3
        else:
            if algo.first_touch_line==2:
                if v>=algo.line1:
                    profit=profit+1
                    algo.second_touch=True
                elif v<=algo.line3:
                    loss=loss+1
                    algo.second_touch=True
            else:
                if v<=algo.line4:
                    profit=profit+1
                    algo.second_touch=True
                elif v>=algo.line2:
                    loss=loss+1
                    algo.second_touch=True
        if algo.second_touch:
            algo.setStartPoint(v)

    print('利差：',licha,'\t盈利:',profit,'\t亏损:',loss)

