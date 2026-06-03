"""
Stock Portfolio Tracker - A Professional Menu-Driven Console Application
Author: Portfolio Tracker Team
Description: This application allows users to manage their stock portfolio with features like
             adding stocks, viewing portfolio, calculating total value, and profit/loss analysis.
             
Features:
    - Add/Remove stocks from portfolio
    - View portfolio with formatted table
    - Calculate total investment value
    - Profit/Loss simulation based on previous prices
    - Save/Load portfolio data (CSV/TXT formats)
    - Input validation and error handling
"""

import csv
import os
from datetime import datetime
from typing import Dict, List, Tuple, Optional

# ============================================================================
# HARDCODED STOCK PRICES DICTIONARY
# ============================================================================
# Current market prices for demonstration purposes
CURRENT_STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

# Previous stock prices for profit/loss calculation
PREVIOUS_STOCK_PRICES = {
    "AAPL": 160,
    "TSLA": 220,
    "GOOGL": 130,
    "MSFT": 300,
    "AMZN": 135
}

# Global portfolio dictionary to store stock data
# Format: {"SYMBOL": quantity, ...}
portfolio = {}

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def clear_screen():
    """Clear the terminal screen for better UI presentation."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title: str) -> None:
    """
    Print a formatted header for sections.
    
    Args:
        title (str): The title to display
    """
    print("\n" + "=" * 70)
    print(f"  {title.center(66)}  ")
    print("=" * 70 + "\n")


def print_divider() -> None:
    """Print a horizontal divider line."""
    print("-" * 70)


def validate_stock_symbol(symbol: str) -> bool:
    """
    Validate if the stock symbol exists in our price dictionary.
    
    Args:
        symbol (str): The stock symbol to validate
        
    Returns:
        bool: True if symbol is valid, False otherwise
    """
    return symbol.upper() in CURRENT_STOCK_PRICES


def validate_quantity(quantity: str) -> Tuple[bool, Optional[float]]:
    """
    Validate if the quantity is a valid positive number.
    
    Args:
        quantity (str): The quantity string to validate
        
    Returns:
        Tuple[bool, Optional[float]]: (is_valid, quantity_value)
    """
    try:
        qty = float(quantity)
        if qty > 0:
            return True, qty
        else:
            print("❌ Error: Quantity must be a positive number!")
            return False, None
    except ValueError:
        print("❌ Error: Invalid quantity! Please enter a valid number.")
        return False, None


# ============================================================================
# CORE PORTFOLIO FUNCTIONS
# ============================================================================

def add_stock() -> None:
    """
    Add a stock to the portfolio with user input validation.
    
    Workflow:
        1. Get stock symbol from user
        2. Validate stock symbol exists
        3. Get quantity from user
        4. Validate quantity is positive
        5. Add or update stock in portfolio
    """
    print_header("ADD STOCK TO PORTFOLIO")
    
    # Display available stocks
    print("📊 Available Stock Symbols:")
    print(", ".join(CURRENT_STOCK_PRICES.keys()))
    print()
    
    try:
        # Get and validate stock symbol
        symbol = input("Enter stock symbol (e.g., AAPL): ").upper().strip()
        
        if not symbol:
            print("❌ Error: Stock symbol cannot be empty!")
            return
            
        if not validate_stock_symbol(symbol):
            print(f"❌ Error: '{symbol}' is not a valid stock symbol!")
            print(f"Available symbols: {', '.join(CURRENT_STOCK_PRICES.keys())}")
            return
        
        # Get and validate quantity
        quantity_input = input(f"Enter quantity for {symbol}: ").strip()
        is_valid, quantity = validate_quantity(quantity_input)
        
        if not is_valid:
            return
        
        # Add or update stock in portfolio
        if symbol in portfolio:
            old_qty = portfolio[symbol]
            portfolio[symbol] += quantity
            print(f"\n✅ Success! Added {quantity} shares of {symbol}")
            print(f"   Previous quantity: {old_qty} → New quantity: {portfolio[symbol]}")
        else:
            portfolio[symbol] = quantity
            print(f"\n✅ Success! Added {quantity} shares of {symbol} to portfolio")
        
    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")


def remove_stock() -> None:
    """
    Remove a stock from the portfolio.
    
    Allows user to:
        1. View current portfolio
        2. Select a stock to remove
        3. Confirm removal
    """
    print_header("REMOVE STOCK FROM PORTFOLIO")
    
    if not portfolio:
        print("❌ Your portfolio is empty! Add stocks first.")
        return
    
    try:
        # Display current portfolio
        print("Current Portfolio:")
        for i, (symbol, qty) in enumerate(portfolio.items(), 1):
            price = CURRENT_STOCK_PRICES.get(symbol, 0)
            value = qty * price
            print(f"{i}. {symbol}: {qty} shares @ ${price}/share = ${value:,.2f}")
        
        print()
        symbol = input("Enter stock symbol to remove: ").upper().strip()
        
        if symbol not in portfolio:
            print(f"❌ Error: {symbol} not found in portfolio!")
            return
        
        # Confirm removal
        qty = portfolio[symbol]
        confirm = input(f"Remove {qty} shares of {symbol}? (yes/no): ").lower().strip()
        
        if confirm == 'yes':
            del portfolio[symbol]
            print(f"✅ Successfully removed {symbol} from portfolio!")
        else:
            print("⚠️  Operation cancelled")
            
    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")


def view_portfolio() -> None:
    """
    Display the current portfolio in a professionally formatted table.
    
    Table shows:
        - Stock Symbol
        - Quantity
        - Current Price
        - Total Value (Quantity × Price)
    """
    print_header("YOUR STOCK PORTFOLIO")
    
    if not portfolio:
        print("📭 Your portfolio is currently empty!")
        print("Use the 'Add Stock' option to get started.\n")
        return
    
    # Prepare table data
    print(f"{'Symbol':<12} {'Quantity':<15} {'Price/Share':<15} {'Total Value':<15}")
    print_divider()
    
    total_value = 0
    
    # Display each stock
    for symbol in sorted(portfolio.keys()):
        quantity = portfolio[symbol]
        price = CURRENT_STOCK_PRICES.get(symbol, 0)
        stock_value = quantity * price
        total_value += stock_value
        
        print(f"{symbol:<12} {quantity:<15.2f} ${price:<14.2f} ${stock_value:<14,.2f}")
    
    print_divider()
    print(f"{'TOTAL PORTFOLIO VALUE':<42} ${total_value:,.2f}")
    print()


def calculate_total() -> None:
    """
    Calculate and display comprehensive portfolio statistics.
    
    Displays:
        - Total portfolio value
        - Average stock price
        - Number of stocks
        - Breakdown by stock
    """
    print_header("PORTFOLIO STATISTICS")
    
    if not portfolio:
        print("📭 Your portfolio is empty! Add stocks to see statistics.\n")
        return
    
    try:
        total_value = 0
        total_quantity = 0
        
        print("Portfolio Breakdown:")
        print_divider()
        
        for symbol in sorted(portfolio.keys()):
            quantity = portfolio[symbol]
            price = CURRENT_STOCK_PRICES.get(symbol, 0)
            stock_value = quantity * price
            
            total_value += stock_value
            total_quantity += quantity
            
            percentage = (stock_value / total_value * 100) if total_value > 0 else 0
            print(f"{symbol}: {quantity:.2f} shares × ${price} = ${stock_value:,.2f} ({percentage:.1f}%)")
        
        print_divider()
        print(f"Total Shares: {total_quantity:.2f}")
        print(f"Total Portfolio Value: ${total_value:,.2f}")
        
        if total_quantity > 0:
            avg_price = total_value / total_quantity
            print(f"Average Price Per Share: ${avg_price:.2f}")
        
        print()
        
    except Exception as e:
        print(f"❌ Error calculating portfolio: {str(e)}")


def profit_loss_simulation() -> None:
    """
    Calculate and display profit/loss simulation based on previous stock prices.
    
    Compares:
        - Previous price vs Current price
        - Shows gain/loss per stock and total
        - Displays percentage change
    """
    print_header("PROFIT/LOSS SIMULATION")
    
    if not portfolio:
        print("📭 Your portfolio is empty! Add stocks to see profit/loss analysis.\n")
        return
    
    try:
        print("Comparing Previous Prices vs Current Prices:")
        print()
        print(f"{'Symbol':<12} {'Quantity':<12} {'Prev Price':<12} {'Curr Price':<12} {'Change':<12} {'P&L':<15}")
        print_divider()
        
        total_profit_loss = 0
        
        for symbol in sorted(portfolio.keys()):
            quantity = portfolio[symbol]
            prev_price = PREVIOUS_STOCK_PRICES.get(symbol, 0)
            curr_price = CURRENT_STOCK_PRICES.get(symbol, 0)
            
            # Calculate profit/loss
            price_diff = curr_price - prev_price
            profit_loss = quantity * price_diff
            change_percent = ((curr_price - prev_price) / prev_price * 100) if prev_price > 0 else 0
            
            total_profit_loss += profit_loss
            
            # Format output
            pl_symbol = "📈" if profit_loss >= 0 else "📉"
            print(f"{symbol:<12} {quantity:<12.2f} ${prev_price:<11.2f} ${curr_price:<11.2f} "
                  f"{change_percent:>+6.2f}% {pl_symbol} ${profit_loss:>+13,.2f}")
        
        print_divider()
        pl_symbol = "📈 GAIN" if total_profit_loss >= 0 else "📉 LOSS"
        print(f"Total Profit/Loss: ${total_profit_loss:>+13,.2f} {pl_symbol}")
        print()
        
    except Exception as e:
        print(f"❌ Error calculating profit/loss: {str(e)}")


# ============================================================================
# FILE OPERATIONS
# ============================================================================

def save_to_csv() -> None:
    """
    Save the current portfolio to a CSV file.
    
    CSV Format:
        Symbol, Quantity, Current Price, Total Value, Previous Price, Profit/Loss
    """
    print_header("SAVE PORTFOLIO TO CSV")
    
    if not portfolio:
        print("❌ Your portfolio is empty! Add stocks before saving.\n")
        return
    
    try:
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"portfolio_{timestamp}.csv"
        filepath = os.path.join("data", filename)
        
        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)
        
        # Write portfolio to CSV
        with open(filepath, 'w', newline='') as csvfile:
            fieldnames = ['Symbol', 'Quantity', 'Current Price', 'Total Value', 
                         'Previous Price', 'Price Change', 'Profit/Loss']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write stock data
            total_value = 0
            total_pl = 0
            
            for symbol in sorted(portfolio.keys()):
                quantity = portfolio[symbol]
                curr_price = CURRENT_STOCK_PRICES.get(symbol, 0)
                prev_price = PREVIOUS_STOCK_PRICES.get(symbol, 0)
                stock_value = quantity * curr_price
                profit_loss = quantity * (curr_price - prev_price)
                
                total_value += stock_value
                total_pl += profit_loss
                
                writer.writerow({
                    'Symbol': symbol,
                    'Quantity': f"{quantity:.2f}",
                    'Current Price': f"${curr_price:.2f}",
                    'Total Value': f"${stock_value:,.2f}",
                    'Previous Price': f"${prev_price:.2f}",
                    'Price Change': f"{((curr_price - prev_price) / prev_price * 100):.2f}%",
                    'Profit/Loss': f"${profit_loss:+,.2f}"
                })
            
            # Write summary
            writer.writerow({})
            writer.writerow({'Symbol': 'TOTAL', 'Total Value': f"${total_value:,.2f}", 
                           'Profit/Loss': f"${total_pl:+,.2f}"})
        
        print(f"✅ Portfolio saved successfully to: {filepath}")
        print(f"   File location: {os.path.abspath(filepath)}\n")
        
    except PermissionError:
        print("❌ Error: Permission denied. Cannot write to file.")
    except Exception as e:
        print(f"❌ Error saving portfolio: {str(e)}")


def save_to_txt() -> None:
    """
    Save the current portfolio to a formatted TXT file.
    
    TXT Format: Human-readable format with clear sections
    """
    print_header("SAVE PORTFOLIO TO TXT")
    
    if not portfolio:
        print("❌ Your portfolio is empty! Add stocks before saving.\n")
        return
    
    try:
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"portfolio_{timestamp}.txt"
        filepath = os.path.join("data", filename)
        
        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)
        
        with open(filepath, 'w') as txtfile:
            # Header
            txtfile.write("=" * 70 + "\n")
            txtfile.write(f"STOCK PORTFOLIO REPORT\n")
            txtfile.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            txtfile.write("=" * 70 + "\n\n")
            
            # Portfolio Details
            txtfile.write("PORTFOLIO DETAILS\n")
            txtfile.write("-" * 70 + "\n")
            txtfile.write(f"{'Symbol':<12} {'Quantity':<15} {'Price/Share':<15} {'Total Value':<15}\n")
            txtfile.write("-" * 70 + "\n")
            
            total_value = 0
            
            for symbol in sorted(portfolio.keys()):
                quantity = portfolio[symbol]
                price = CURRENT_STOCK_PRICES.get(symbol, 0)
                stock_value = quantity * price
                total_value += stock_value
                
                txtfile.write(f"{symbol:<12} {quantity:<15.2f} ${price:<14.2f} ${stock_value:<14,.2f}\n")
            
            txtfile.write("-" * 70 + "\n")
            txtfile.write(f"TOTAL PORTFOLIO VALUE: ${total_value:,.2f}\n\n")
            
            # Profit/Loss Analysis
            txtfile.write("PROFIT/LOSS ANALYSIS\n")
            txtfile.write("-" * 70 + "\n")
            txtfile.write(f"{'Symbol':<12} {'Prev Price':<12} {'Curr Price':<12} {'Change':<12} {'P&L':<15}\n")
            txtfile.write("-" * 70 + "\n")
            
            total_pl = 0
            
            for symbol in sorted(portfolio.keys()):
                quantity = portfolio[symbol]
                prev_price = PREVIOUS_STOCK_PRICES.get(symbol, 0)
                curr_price = CURRENT_STOCK_PRICES.get(symbol, 0)
                profit_loss = quantity * (curr_price - prev_price)
                change_percent = ((curr_price - prev_price) / prev_price * 100) if prev_price > 0 else 0
                
                total_pl += profit_loss
                
                txtfile.write(f"{symbol:<12} ${prev_price:<11.2f} ${curr_price:<11.2f} "
                            f"{change_percent:>+6.2f}% ${profit_loss:>+13,.2f}\n")
            
            txtfile.write("-" * 70 + "\n")
            txtfile.write(f"TOTAL PROFIT/LOSS: ${total_pl:+,.2f}\n")
        
        print(f"✅ Portfolio saved successfully to: {filepath}")
        print(f"   File location: {os.path.abspath(filepath)}\n")
        
    except PermissionError:
        print("❌ Error: Permission denied. Cannot write to file.")
    except Exception as e:
        print(f"❌ Error saving portfolio: {str(e)}")


def load_portfolio_from_csv() -> None:
    """
    Load portfolio from a CSV file (if available in data directory).
    """
    print_header("LOAD PORTFOLIO FROM CSV")
    
    try:
        # List available CSV files
        data_dir = "data"
        if not os.path.exists(data_dir):
            print("❌ No saved portfolios found. The 'data' directory doesn't exist.\n")
            return
        
        csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
        
        if not csv_files:
            print("❌ No CSV files found in the 'data' directory.\n")
            return
        
        print("Available portfolios:")
        for i, file in enumerate(csv_files, 1):
            print(f"{i}. {file}")
        
        try:
            choice = int(input("\nSelect portfolio number: "))
            if 1 <= choice <= len(csv_files):
                filepath = os.path.join(data_dir, csv_files[choice - 1])
                
                # Load portfolio
                global portfolio
                portfolio = {}
                
                with open(filepath, 'r') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if row.get('Symbol') and row.get('Symbol') != 'TOTAL':
                            try:
                                qty = float(row['Quantity'])
                                portfolio[row['Symbol']] = qty
                            except ValueError:
                                continue
                
                print(f"✅ Portfolio loaded successfully from {csv_files[choice - 1]}")
                print(f"   Total stocks loaded: {len(portfolio)}\n")
            else:
                print("❌ Invalid selection!\n")
        except ValueError:
            print("❌ Invalid input!\n")
            
    except Exception as e:
        print(f"❌ Error loading portfolio: {str(e)}")


# ============================================================================
# MAIN MENU AND APPLICATION FLOW
# ============================================================================

def display_menu() -> None:
    """Display the main menu options."""
    print_header("STOCK PORTFOLIO TRACKER - MAIN MENU")
    print("""
    1. 📈 Add Stock to Portfolio
    2. 👁️  View Portfolio
    3. 🗑️  Remove Stock from Portfolio
    4. 💰 Calculate Portfolio Total
    5. 📊 Profit/Loss Simulation
    6. 💾 Save Portfolio to CSV
    7. 📄 Save Portfolio to TXT
    8. 📂 Load Portfolio from CSV
    9. ℹ️  Show Available Stocks & Prices
    10. 🚪 Exit
    """)


def show_available_stocks() -> None:
    """Display available stocks and their current/previous prices."""
    print_header("AVAILABLE STOCKS & PRICES")
    
    print(f"{'Symbol':<12} {'Current Price':<15} {'Previous Price':<15} {'Change':<15}")
    print_divider()
    
    for symbol in sorted(CURRENT_STOCK_PRICES.keys()):
        curr = CURRENT_STOCK_PRICES[symbol]
        prev = PREVIOUS_STOCK_PRICES[symbol]
        change = ((curr - prev) / prev * 100) if prev > 0 else 0
        change_symbol = "📈" if change >= 0 else "📉"
        
        print(f"{symbol:<12} ${curr:<14.2f} ${prev:<14.2f} {change:>+6.2f}% {change_symbol}")
    print()


def main():
    """
    Main application loop.
    
    Workflow:
        1. Display welcome message
        2. Show menu options
        3. Get user input
        4. Execute selected operation
        5. Repeat until user exits
    """
    
    # Welcome message
    clear_screen()
    print("\n" + "=" * 70)
    print("  WELCOME TO STOCK PORTFOLIO TRACKER ".center(70))
    print("  Professional Portfolio Management System ".center(70))
    print("=" * 70)
    print("\nStart building your investment portfolio today!")
    print("Press Enter to continue...")
    input()
    
    # Main loop
    while True:
        clear_screen()
        display_menu()
        
        try:
            choice = input("Enter your choice (1-10): ").strip()
            
            if choice == '1':
                clear_screen()
                add_stock()
            elif choice == '2':
                clear_screen()
                view_portfolio()
            elif choice == '3':
                clear_screen()
                remove_stock()
            elif choice == '4':
                clear_screen()
                calculate_total()
            elif choice == '5':
                clear_screen()
                profit_loss_simulation()
            elif choice == '6':
                clear_screen()
                save_to_csv()
            elif choice == '7':
                clear_screen()
                save_to_txt()
            elif choice == '8':
                clear_screen()
                load_portfolio_from_csv()
            elif choice == '9':
                clear_screen()
                show_available_stocks()
            elif choice == '10':
                print_header("Thank You!")
                print("Thanks for using Stock Portfolio Tracker!")
                print("Your investment journey matters. Happy investing! 📈\n")
                break
            else:
                clear_screen()
                print("❌ Invalid choice! Please enter a number between 1 and 10.")
                print("Press Enter to continue...")
                input()
                continue
            
            print("Press Enter to continue...")
            input()
            
        except KeyboardInterrupt:
            clear_screen()
            print("\n⚠️  Application interrupted by user.")
            print("Exiting Stock Portfolio Tracker...\n")
            break
        except Exception as e:
            clear_screen()
            print(f"❌ An unexpected error occurred: {str(e)}")
            print("Press Enter to continue...")
            input()


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
