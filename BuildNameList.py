import tushare as ts
ts.set_token('d7e28c79162bc5a6fd505e5183c7d9fe45ef6fb84c2eef01b8b25bf5')
pro = ts.pro_api()




data = pro.stock_basic(exchange_id='', is_hs='', fields='symbol,name,list_date,list_status')

data.to_csv('./Data/stockList.csv')