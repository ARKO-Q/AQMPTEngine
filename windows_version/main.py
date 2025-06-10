import os
from dependencies.data import *
from dependencies.sim import *
from dependencies.graphics import *

assets = []
correct_selection = False
while correct_selection == False:
    os.system('clear')
    print('ARKO Quantum S.R.L. Modern Portfolio Theory Engine                https://arkoquantum.com')
    print('──────────────────────────────────────────────────────────────────────────────────────────┤')
    try:
        num_assets          = int(input('# of Instruments   : '))
        num_simulations     = int(input('# of Simulations   : '))
        for asset in range(num_assets):
            ticker = input(f'Ticker #{asset + 1}          : ')
            assets.append(ticker)
    except ValueError:
         input('\nValue Error: Incorrect data type, review documentation. \nPress ENTER to restart: ')
         continue
    except:
        input('Unkown Error: Revise input values, review documentation. \nPress ENTER to restart: ')
        continue
    
    print('──────────────────────────────────────────────────────────────────────────────────────────┤')
    confirmation = input('Correct Selection? (Y/N): ')
    if confirmation == 'y' or confirmation == 'Y':
        correct_selection = True
    else:
        continue

print('\nLoading Historical Data...')

data = organize_data(assets)

print('──────────────────────────────────────────────────────────────────────────────────────────┤')

parameters = calculate_parameters(data)

portfolios = simulate_portfolios(assets, num_simulations)
results = calculate_performance_metrics(parameters, portfolios)

returns = [res['mean_return'] for res in results]
volatilities = [res['volatility'] for res in results]
sharpes = [res['sharpe'] for res in results]

max_sharpe_idx = sharpes.index(max(sharpes))
min_vol_idx = volatilities.index(min(volatilities))
max_return_idx = returns.index(max(returns))

selected = [
    ('Max Sharpe Ratio Portfolio', results[max_sharpe_idx]),
    ('Min Volatility Portfolio', results[min_vol_idx]),
    ('Max Mean Return Portfolio', results[max_return_idx])
]

for idx, (name, portfolio) in enumerate(selected):
    if idx == 0:
        print(f'\n{name}:')
    else:
        print(f'\n\n{name}:')
    for k, v in portfolio.items():
        if k != 'weights':
            metric_name = k.replace('_', ' ').title()
            if isinstance(v, float):
                print(f'  {metric_name}: {v:.4f}', end=' ')
            else:
                print(f'  {metric_name}: {v}', end=' ')
    print()
    print('  Weights:', end='')
    for ticker, weight in zip(assets, portfolio['weights']):
        print(f' {ticker} {weight * 100:.2f}%', end=' ')

print()

plot_efficient_frontier(results)