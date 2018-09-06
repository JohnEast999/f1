## 生成 Data/stockList 所有股票名称

import tushare as ts
import pandas as pd
from itertools import islice

ts.set_token('d7e28c79162bc5a6fd505e5183c7d9fe45ef6fb84c2eef01b8b25bf5')
pro = ts.pro_api()

stockList = '../Data/stockList.csv'
a = pd.read_csv(stockList, encoding='utf-8')

# print(a['ts_code'])

count = 0
for this_ts_code in a['ts_code']:
    count = count + 1

    df = pro.top10_holders(ts_code=this_ts_code,start_date='20170101', end_date='20171231')

    if count == 1 :
        df.to_csv('../Data/stockHolder.csv')
    else:
        df.to_csv('../Data/stockHolder.csv', mode='a', header=None)
