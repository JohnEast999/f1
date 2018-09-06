## 生成 Data/stockList 所有股票名称

import tushare as ts
import pandas as pd

ts.set_token('d7e28c79162bc5a6fd505e5183c7d9fe45ef6fb84c2eef01b8b25bf5')
pro = ts.pro_api()

stockList = '../Data/stockList.csv'
a = pd.read_csv(stockList, encoding='utf-8')

print(a['ts_code'])

for this_ts_code in a['ts_code']:
    print(this_ts_code)