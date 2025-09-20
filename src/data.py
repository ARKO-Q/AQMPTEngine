import yfinance as yf
import pandas as pd

def organize_data(assets):
    'pull data from yfinance and return a dataframe with adjusted close prices'
    price_data = []

    for stock in assets:
        data = yf.download(stock, auto_adjust=False)
        adj_close = data[['Adj Close']].rename(columns={'Adj Close': stock})
        price_data.append(adj_close)

    table = pd.concat(price_data, axis=1, join='inner')

    return table

def get_risk_free_rate():
    'get the latest risk free rate from FRED'
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10"
    df = pd.read_csv(url)
    df = df.dropna()
    latest_rate = df['DGS10'].iloc[-1]

    return float(latest_rate) / 100

def calculate_parameters(data):
    'calculate parameters for the portfolio'

    parameters = {}

    ret = data.pct_change()
    ret.dropna(inplace=True)
    mean_ret = ret.mean()
    cov = ret.cov()
    corr = ret.corr()
    risk_free_rate = get_risk_free_rate()

    parameters.update({'returns': ret})
    parameters.update({'mean_returns': mean_ret})
    parameters.update({'covariance': cov})
    parameters.update({'correlation': corr})
    parameters.update({'risk_free_rate': risk_free_rate})

    return parameters