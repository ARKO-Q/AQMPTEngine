import numpy as np

def simulate_portfolios(assets, runs):
    'Simulate random portfolios and return a list of weights for each portfolio'

    weights_list = []

    for i in range(runs):
        weights = np.random.random(len(assets))
        weights /= np.sum(weights)

        weights_list.append(weights)

    return weights_list

def calculate_performance_metrics(parameters, portfolios):
    'Calculate and return performance metrics for the simulated portfolios'
    portfolio_list = []

    mean_ret = parameters['mean_returns']
    cov = parameters['covariance']
    rf = parameters['risk_free_rate']

    trading_days = 252

    for portfolio in portfolios:
        model = {}
        mean_return = float(np.dot(portfolio, mean_ret))
        volatility = float(np.sqrt(np.dot(portfolio.T, np.dot(cov, portfolio))))

        annualized_return = mean_return * trading_days
        annualized_volatility = volatility * (trading_days ** 0.5)
        sharpe = float((annualized_return - rf) / annualized_volatility) if annualized_volatility != 0 else 0.0
        weights = [float(w) for w in portfolio]

        model.update({'mean_return': annualized_return})
        model.update({'volatility': annualized_volatility})
        model.update({'sharpe': sharpe})
        model.update({'weights': weights})

        portfolio_list.append(model)

    return portfolio_list