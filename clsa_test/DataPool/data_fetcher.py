from pytickersymbols import PyTickerSymbols
import yfinance as yf
import logging
logger=logging.getLogger('DataFetcher')
import pandas as pd

def get_index_comp_latest(index_name:str):
    '''
    get latest index components
    :param index_name:
    :return: list of infos of each comp
    '''
    fetcher=PyTickerSymbols()
    info=list(fetcher.get_stocks_by_index(index_name))
    if len(info)==0:
        logger.warning('got no info,pls check your index_name or package availability')
    return info

def get_stock_kline(symbol_list:list,start_date:int,end_date:int):
    '''
    get kline data for all symbols in the list

    :param symbol_list: a list of symbols
    :param start_date: start date of kline (include)
    :param end_date: end date of kline (include)
    :return: a composite dataframe that contains all klines
    '''
    assert start_date<=end_date,f'start_date({start_date}) should smaller than end_date({end_date})'
    stdate_str=(pd.to_datetime(str(start_date))-pd.DateOffset(days=1)).strftime('%Y-%m-%d')
    eddate_str=(pd.to_datetime(str(end_date))+pd.DateOffset(days=1)).strftime('%Y-%m-%d')
    data=yf.download(' '.join(symbol_list),
                           start=stdate_str,
                           end=eddate_str,
                           auto_adjust=True)
    data=data.loc[str(start_date):str(end_date)]
    return data


if __name__=='__main__':
    sinfos=get_index_comp_latest('S&P 100')
    slist=[i['symbol'] for i in sinfos]
    data=get_stock_kline(slist,20200101,20210701)
    data.to_pickle('sp100_klines_adjusted.pkl')
    print(data.shape)


