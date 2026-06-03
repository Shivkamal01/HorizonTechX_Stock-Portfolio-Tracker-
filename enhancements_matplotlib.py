"""
Optional Enhancement: Data Visualization with Matplotlib
File: enhancements_matplotlib.py

This module demonstrates how to create charts and visualizations for the 
Stock Portfolio Tracker using matplotlib library.

To use this: pip install matplotlib

Integration: Add these functions to your main application for visual analysis
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List, Tuple


# ============================================================================
# PORTFOLIO VISUALIZATION FUNCTIONS
# ============================================================================

def create_portfolio_pie_chart(portfolio: Dict[str, float], 
                               stock_prices: Dict[str, float]) -> None:
    """
    Create a pie chart showing portfolio allocation by value.
    
    Args:
        portfolio (Dict): Dictionary of {symbol: quantity}
        stock_prices (Dict): Dictionary of {symbol: price}
    
    Example:
        >>> portfolio = {"AAPL": 10, "TSLA": 5, "GOOGL": 15}
        >>> prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140}
        >>> create_portfolio_pie_chart(portfolio, prices)
    """
    if not portfolio:
        print("❌ Portfolio is empty. Cannot create chart.")
        return
    
    # Calculate values
    symbols = list(portfolio.keys())
    values = [portfolio[s] * stock_prices.get(s, 0) for s in symbols]
    
    # Create pie chart
    plt.figure(figsize=(10, 8))
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    
    plt.pie(values, labels=symbols, autopct='%1.1f%%', 
            startangle=90, colors=colors[:len(symbols)])
    
    plt.title('Stock Portfolio Allocation by Value', fontsize=16, fontweight='bold')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    
    plt.tight_layout()
    plt.show()


def create_portfolio_bar_chart(portfolio: Dict[str, float], 
                               stock_prices: Dict[str, float]) -> None:
    """
    Create a bar chart showing stock values.
    
    Args:
        portfolio (Dict): Dictionary of {symbol: quantity}
        stock_prices (Dict): Dictionary of {symbol: price}
    
    Example:
        >>> create_portfolio_bar_chart(portfolio, prices)
    """
    if not portfolio:
        print("❌ Portfolio is empty. Cannot create chart.")
        return
    
    # Prepare data
    symbols = list(portfolio.keys())
    values = [portfolio[s] * stock_prices.get(s, 0) for s in symbols]
    
    # Create bar chart
    plt.figure(figsize=(12, 6))
    bars = plt.bar(symbols, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'][:len(symbols)])
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'${height:,.0f}',
                ha='center', va='bottom', fontweight='bold')
    
    plt.xlabel('Stock Symbol', fontsize=12, fontweight='bold')
    plt.ylabel('Portfolio Value ($)', fontsize=12, fontweight='bold')
    plt.title('Stock Portfolio Value Distribution', fontsize=16, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def create_profit_loss_chart(portfolio: Dict[str, float],
                             current_prices: Dict[str, float],
                             previous_prices: Dict[str, float]) -> None:
    """
    Create a bar chart showing profit/loss by stock.
    
    Args:
        portfolio (Dict): Dictionary of {symbol: quantity}
        current_prices (Dict): Dictionary of {symbol: current_price}
        previous_prices (Dict): Dictionary of {symbol: previous_price}
    
    Example:
        >>> create_profit_loss_chart(portfolio, current, previous)
    """
    if not portfolio:
        print("❌ Portfolio is empty. Cannot create chart.")
        return
    
    # Calculate P&L
    symbols = list(portfolio.keys())
    pl_values = []
    
    for symbol in symbols:
        qty = portfolio[symbol]
        current = current_prices.get(symbol, 0)
        previous = previous_prices.get(symbol, 0)
        pl = qty * (current - previous)
        pl_values.append(pl)
    
    # Create bar chart with profit/loss colors
    plt.figure(figsize=(12, 6))
    colors = ['#4ECDC4' if x >= 0 else '#FF6B6B' for x in pl_values]
    bars = plt.bar(symbols, pl_values, color=colors)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        label = f'${height:,.0f}'
        y_pos = height if height >= 0 else height
        va = 'bottom' if height >= 0 else 'top'
        
        plt.text(bar.get_x() + bar.get_width()/2., y_pos,
                label, ha='center', va=va, fontweight='bold')
    
    plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
    plt.xlabel('Stock Symbol', fontsize=12, fontweight='bold')
    plt.ylabel('Profit/Loss ($)', fontsize=12, fontweight='bold')
    plt.title('Profit/Loss by Stock', fontsize=16, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def create_price_comparison_chart(current_prices: Dict[str, float],
                                  previous_prices: Dict[str, float]) -> None:
    """
    Create a grouped bar chart comparing previous vs current prices.
    
    Args:
        current_prices (Dict): Dictionary of {symbol: current_price}
        previous_prices (Dict): Dictionary of {symbol: previous_price}
    
    Example:
        >>> create_price_comparison_chart(current, previous)
    """
    symbols = list(current_prices.keys())
    current = [current_prices[s] for s in symbols]
    previous = [previous_prices.get(s, 0) for s in symbols]
    
    # Create grouped bar chart
    x = np.arange(len(symbols))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(12, 6))
    bars1 = ax.bar(x - width/2, previous, width, label='Previous Price', color='#95B8D1')
    bars2 = ax.bar(x + width/2, current, width, label='Current Price', color='#4ECDC4')
    
    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'${height:.0f}',
                   ha='center', va='bottom', fontsize=9)
    
    ax.set_xlabel('Stock Symbol', fontsize=12, fontweight='bold')
    ax.set_ylabel('Price ($)', fontsize=12, fontweight='bold')
    ax.set_title('Price Comparison: Previous vs Current', fontsize=16, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(symbols)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def create_percentage_change_chart(current_prices: Dict[str, float],
                                   previous_prices: Dict[str, float]) -> None:
    """
    Create a bar chart showing percentage change for each stock.
    
    Args:
        current_prices (Dict): Dictionary of {symbol: current_price}
        previous_prices (Dict): Dictionary of {symbol: previous_price}
    
    Example:
        >>> create_percentage_change_chart(current, previous)
    """
    symbols = list(current_prices.keys())
    changes = []
    
    for symbol in symbols:
        current = current_prices[symbol]
        previous = previous_prices.get(symbol, current)
        
        if previous > 0:
            change = ((current - previous) / previous) * 100
        else:
            change = 0
        changes.append(change)
    
    # Create bar chart
    plt.figure(figsize=(12, 6))
    colors = ['#4ECDC4' if x >= 0 else '#FF6B6B' for x in changes]
    bars = plt.bar(symbols, changes, color=colors)
    
    # Add percentage labels
    for bar in bars:
        height = bar.get_height()
        label = f'{height:+.1f}%'
        y_pos = height if height >= 0 else height
        va = 'bottom' if height >= 0 else 'top'
        
        plt.text(bar.get_x() + bar.get_width()/2., y_pos,
                label, ha='center', va=va, fontweight='bold')
    
    plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
    plt.xlabel('Stock Symbol', fontsize=12, fontweight='bold')
    plt.ylabel('Price Change (%)', fontsize=12, fontweight='bold')
    plt.title('Stock Price Percentage Change', fontsize=16, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def create_cumulative_value_chart(portfolio: Dict[str, float],
                                  stock_prices: Dict[str, float]) -> None:
    """
    Create a line chart showing cumulative portfolio value by stock (stacked).
    
    Args:
        portfolio (Dict): Dictionary of {symbol: quantity}
        stock_prices (Dict): Dictionary of {symbol: price}
    
    Example:
        >>> create_cumulative_value_chart(portfolio, prices)
    """
    if not portfolio:
        print("❌ Portfolio is empty. Cannot create chart.")
        return
    
    # Sort by value
    sorted_stocks = sorted(portfolio.items(), 
                          key=lambda x: x[1] * stock_prices.get(x[0], 0), 
                          reverse=True)
    
    symbols = [stock[0] for stock in sorted_stocks]
    values = [stock[1] * stock_prices.get(stock[0], 0) for stock in sorted_stocks]
    
    # Calculate cumulative
    cumulative = np.cumsum(values)
    
    # Create stacked area chart
    plt.figure(figsize=(12, 6))
    
    # Create the plot
    bottom = 0
    colors_list = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    
    for i, (symbol, value) in enumerate(zip(symbols, values)):
        plt.bar(i, value, bottom=bottom, label=symbol, color=colors_list[i % len(colors_list)])
        
        # Add label
        plt.text(i, bottom + value/2, f'${value:,.0f}', 
                ha='center', va='center', fontweight='bold', color='white')
        bottom += value
    
    plt.xticks(range(len(symbols)), symbols)
    plt.ylabel('Value ($)', fontsize=12, fontweight='bold')
    plt.title('Portfolio Composition (Stacked)', fontsize=16, fontweight='bold')
    plt.legend(loc='upper left')
    plt.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.show()


# ============================================================================
# INTEGRATION INSTRUCTIONS
# ============================================================================

"""
To add matplotlib visualizations to your application:

1. Install matplotlib:
   pip install matplotlib

2. Add this import to stock_portfolio_tracker.py:
   from enhancements_matplotlib import (
       create_portfolio_pie_chart,
       create_portfolio_bar_chart,
       create_profit_loss_chart,
       create_price_comparison_chart,
       create_percentage_change_chart
   )

3. Add a new menu option (after option 9) for visualizations:
   
   elif choice == '10':
       clear_screen()
       print_header("PORTFOLIO VISUALIZATIONS")
       print("1. Portfolio Allocation (Pie Chart)")
       print("2. Stock Values (Bar Chart)")
       print("3. Profit/Loss Analysis (Bar Chart)")
       print("4. Price Comparison (Grouped Bars)")
       print("5. Percentage Change (Bar Chart)")
       sub_choice = input("Select visualization: ")
       
       if sub_choice == '1':
           create_portfolio_pie_chart(portfolio, CURRENT_STOCK_PRICES)
       elif sub_choice == '2':
           create_portfolio_bar_chart(portfolio, CURRENT_STOCK_PRICES)
       elif sub_choice == '3':
           create_profit_loss_chart(portfolio, CURRENT_STOCK_PRICES, PREVIOUS_STOCK_PRICES)
       elif sub_choice == '4':
           create_price_comparison_chart(CURRENT_STOCK_PRICES, PREVIOUS_STOCK_PRICES)
       elif sub_choice == '5':
           create_percentage_change_chart(CURRENT_STOCK_PRICES, PREVIOUS_STOCK_PRICES)

4. Available visualizations:
   - Pie Chart: Shows portfolio allocation percentages
   - Bar Chart: Shows stock values
   - P&L Chart: Shows profit/loss by stock
   - Comparison Chart: Previous vs Current prices
   - Percentage Change: Shows % price changes
   - Cumulative Value: Stacked view of portfolio

5. Colors used:
   - Gain/Positive: #4ECDC4 (Teal)
   - Loss/Negative: #FF6B6B (Red)
   - Primary: #45B7D1 (Blue)
   - Accent 1: #FFA07A (Light Salmon)
   - Accent 2: #98D8C8 (Mint)

6. Example call:
   >>> portfolio = {"AAPL": 10, "TSLA": 5}
   >>> prices = {"AAPL": 180, "TSLA": 250}
   >>> create_portfolio_pie_chart(portfolio, prices)
"""
