import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def plot_efficient_frontier(sim_results):
    'Plots the efficient frontier and simulated portfolios using matplotlib'

    returns = [res['mean_return'] for res in sim_results]
    volatilities = [res['volatility'] for res in sim_results]
    sharpes = [res['sharpe'] for res in sim_results]

    max_sharpe_idx = sharpes.index(max(sharpes))
    max_sharpe_return = returns[max_sharpe_idx]
    max_sharpe_volatility = volatilities[max_sharpe_idx]

    min_vol_idx = volatilities.index(min(volatilities))
    min_vol_return = returns[min_vol_idx]
    min_vol_volatility = volatilities[min_vol_idx]

    max_return_idx = returns.index(max(returns))
    max_return = returns[max_return_idx]
    max_return_volatility = volatilities[max_return_idx]

    plt.figure(figsize= (10, 6))
    fig = plt.gcf()
    fig.canvas.manager.set_window_title('ARKO Quantum S.R.L. Modern Portfolio Theory Engine - Efficient Frontier Curve Graphic')

    ax = plt.gca()
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')

    scatter = plt.scatter(
    volatilities, returns, c = sharpes, cmap = 'YlGnBu', marker = 'o', s = 20, alpha = 0.6,
    edgecolor = 'none', linewidth=0.5, label = 'Simulated Portfolios'
    )

    plt.scatter(max_sharpe_volatility, max_sharpe_return, marker = '*', color ='red', s=200, edgecolor = 'none', linewidth = 1.5, label = 'Max Sharpe Ratio')
    plt.scatter(min_vol_volatility, min_vol_return, marker = 'D', color = 'orange', s=120, edgecolor ='none', linewidth = 1.5, label = 'Min Volatility')
    plt.scatter(max_return_volatility, max_return, marker = '^', color = 'purple', s=120, edgecolor ='none', linewidth = 1.5, label = 'Max Mean Return')
    
    plt.legend(loc = 'upper left', facecolor = 'black')
    
    plt.title('ARKO Quantum S.R.L - Efficient Frontier Curve', color = 'white')
    plt.xlabel('Annualized Volatility (δ)', color = 'white')
    plt.ylabel('Annualized Mean Return (μ)', color = 'white')

    ax.tick_params(colors = 'white')
    plt.grid(True, color = 'white', linestyle = '--', linewidth = 0.5)
    plt.legend(loc = 'upper left', facecolor = 'black', edgecolor = 'white', labelcolor = 'white')

    cbar = plt.colorbar(scatter, label = 'Sharpe Ratio (μ/δ)')
    cbar.ax.yaxis.set_tick_params(color = 'white')
    plt.setp(cbar.ax.get_yticklabels(), color = 'white')
    cbar.set_label('Sharpe Ratio (μ/δ)', color = 'white')

    plt.show()