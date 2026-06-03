"""
Optional Enhancement: Colorized Terminal Output
File: stock_portfolio_tracker_with_colors.py

This module demonstrates how to add colorized output to the Stock Portfolio Tracker
using the colorama library for enhanced visual appeal.

To use this: pip install colorama

Integration instructions:
1. Install colorama: pip install colorama
2. Import at the top of stock_portfolio_tracker.py:
   from colorama import Fore, Back, Style, init
   
3. Initialize colorama in the main() function:
   init(autoreset=True)
   
4. Replace print statements as shown below
"""

# Import required module
from colorama import Fore, Back, Style, init

# Initialize colorama (call this at application start)
def initialize_colorama():
    """Initialize colorama for cross-platform colored output."""
    init(autoreset=True)


# ============================================================================
# COLORED OUTPUT EXAMPLES
# ============================================================================

def print_header_colored(title: str) -> None:
    """Print a colored header."""
    print(f"\n{Back.BLUE}{Fore.WHITE}{'=' * 70}{Style.RESET_ALL}")
    print(f"{Back.BLUE}{Fore.WHITE}{title.center(70)}{Style.RESET_ALL}")
    print(f"{Back.BLUE}{Fore.WHITE}{'=' * 70}{Style.RESET_ALL}\n")


def print_success(message: str) -> None:
    """Print success message in green."""
    print(f"{Fore.GREEN}✅ {message}{Style.RESET_ALL}")


def print_error(message: str) -> None:
    """Print error message in red."""
    print(f"{Fore.RED}❌ {message}{Style.RESET_ALL}")


def print_warning(message: str) -> None:
    """Print warning message in yellow."""
    print(f"{Fore.YELLOW}⚠️  {message}{Style.RESET_ALL}")


def print_info(message: str) -> None:
    """Print info message in cyan."""
    print(f"{Fore.CYAN}ℹ️  {message}{Style.RESET_ALL}")


def print_profit_colored(value: float, quantity: int, symbol: str) -> None:
    """Print profit/loss with appropriate color."""
    if value >= 0:
        print(f"{Fore.GREEN}📈 {symbol}: {quantity} shares = {Fore.GREEN}+${value:,.2f}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}📉 {symbol}: {quantity} shares = {Fore.RED}-${abs(value):,.2f}{Style.RESET_ALL}")


def print_portfolio_colored():
    """Print colored portfolio header and divider."""
    print(f"{Fore.CYAN}{'Symbol':<12} {'Quantity':<15} {'Price/Share':<15} {'Total Value':<15}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{'-' * 70}{Style.RESET_ALL}")


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

def example_colored_output():
    """Demonstrate colored output."""
    
    # Initialize
    initialize_colorama()
    
    # Examples
    print_header_colored("COLORED OUTPUT EXAMPLES")
    
    print_success("Portfolio loaded successfully!")
    print_error("Invalid stock symbol!")
    print_warning("This operation cannot be undone")
    print_info("3 stocks are in your portfolio")
    
    print_profit_colored(200, 10, "AAPL")
    print_profit_colored(-50, 5, "TSLA")
    
    print_portfolio_colored()
    print(f"{'AAPL':<12} {'10.00':<15} {'$180.00':<15} {'$1,800.00':<15}")


# ============================================================================
# INTEGRATION CHECKLIST
# ============================================================================

"""
To add colorized output to your application:

1. Install colorama:
   pip install colorama

2. Add at the top of stock_portfolio_tracker.py:
   from colorama import Fore, Back, Style, init

3. In the main() function, add:
   init(autoreset=True)  # Initialize at app start

4. Replace print statements throughout:
   
   BEFORE:
   print("✅ Success!")
   
   AFTER:
   print(f"{Fore.GREEN}✅ Success!{Style.RESET_ALL}")

5. Color options:
   - Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW
   - Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE
   - Back.BLACK, Back.RED, Back.GREEN (for background colors)
   - Style.BRIGHT, Style.DIM, Style.NORMAL, Style.RESET_ALL

6. Common patterns:
   Success:   f"{Fore.GREEN}✅ Message{Style.RESET_ALL}"
   Error:     f"{Fore.RED}❌ Message{Style.RESET_ALL}"
   Warning:   f"{Fore.YELLOW}⚠️ Message{Style.RESET_ALL}"
   Info:      f"{Fore.CYAN}ℹ️ Message{Style.RESET_ALL}"
   Header:    f"{Back.BLUE}{Fore.WHITE}Text{Style.RESET_ALL}"
"""
