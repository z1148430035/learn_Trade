from futu import*
import pandas as pd

pd.set_option('display.float_format','{:.1f}'.format)


def getStockData(stratDate,endData,stock_code):
    quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
    ret, data, page_req_key = quote_ctx.request_history_kline(stock_code, start=stratDate, end=endData)  # 每页5个，请求第一页
    if ret == RET_OK:
        
        data = pd.DataFrame(data)
        data['time_key'] = pd.to_datetime(data['time_key'])
        data.rename(columns={'time_key':'date'},inplace=True)
        data.set_index('date',inplace = True)
        df = pd.DataFrame(index = data.index)
        df['open'] = data['open']
        df['close'] = data['close']
        df['high'] = data['high']
        df['low'] = data['low']
        df['turnover'] = data['turnover']
        #此处修改要添加的列
        print("数据成功获取")
        return data,df
       
    else:
        print('error:', data)
        
    quote_ctx.close()


def main():
    stock_code = 'HK.00700'
    startDate = '2024-01-01'
    endDate = '2024-12-31'

    data,df = getStockData(startDate,endDate,stock_code)
    if data is not None:
        print(data)
        print(df)
    else:
        print("检查数据")

if __name__ == "__main__":
    main()
