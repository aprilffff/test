import pandas as pd

def momentum_strat(top_k,signal):
    '''
    a simple momentum model that buy top_k stocks based on the ranking of daily_return(multiple days) every morning;
    daily_return is calculated with prev_close;
    :param top_k: number of top ranking stocks to buy
    :param o2oret_1day: number of days to calculate daily_return
    :return: weight to hold for each stock
    '''
    wgt=signal.rank(axis=1,ascending=False)<=top_k
    wgt=wgt.astype(int)/top_k

    return wgt

if __name__=='__main__':
    signal=pd.read_pickle('../FeaturePool/c2cret_5day.pkl')
    top_k=10
    wgt=momentum_strat(top_k,signal)


