

def daily_c2c_return(close_df,days=1,**kwargs):
    '''
    return close to close return
    :param close_df: close price in format of dataframe
    :param days: number of days to calculate  return
    :return: a single dataframe of this feature
    '''
    res=close_df.sort_index().pct_change(days)
    return res



def daily_o2o_return(open_df,days=1,**kwargs):
    '''
    return open to open return
    :param open_df: open price in format of dataframe
    :param days: number of days to calculate the return
    :return: a single dataframe of this feature
    '''
    res=open_df.sort_index().pct_change(days)
    return res


if __name__=='__main__':
    import pandas as pd
    kline=pd.read_pickle('../DataPool/sp100_klines_adjusted.pkl')
    cp=kline.xs('Close',axis=1,level=0)
    c2cret_5day=daily_c2c_return(cp,days=5)
    c2cret_5day.to_pickle('c2cret_5day.pkl')

    op=kline.xs('Open',axis=1,level=0)
    o2oret_1day=daily_o2o_return(op,days=1)
    o2oret_1day.to_pickle('o2oret_1day.pkl')