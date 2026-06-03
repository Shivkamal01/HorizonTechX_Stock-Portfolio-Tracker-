# Stock Portfolio Tracker 📈

A professional, beginner-friendly Python console application for managing your stock investment portfolio with real-time calculations and profit/loss analysis.

## 🎯 Overview

Stock Portfolio Tracker is a menu-driven application designed for investors who want to:
- Add and manage multiple stocks in their portfolio
- Track individual stock values and total portfolio worth
- Analyze profit/loss based on previous prices
- Save portfolio data in CSV or TXT formats
- View portfolio in a professionally formatted table

**Perfect for:** Beginners learning Python, students, and anyone wanting to track stock investments.

---

## ✨ Features

### Core Features
1. **Add Stocks** - Add stocks with quantities to your portfolio
2. **View Portfolio** - Display portfolio in a formatted table showing symbols, quantities, prices, and values
3. **Remove Stocks** - Remove stocks from your portfolio with confirmation
4. **Calculate Total** - View comprehensive portfolio statistics and breakdowns
5. **Profit/Loss Simulation** - Compare previous prices with current prices to analyze gains/losses
6. **Save to CSV** - Export portfolio to CSV format with full data
7. **Save to TXT** - Export portfolio to human-readable TXT format
8. **Load from CSV** - Load previously saved portfolios
9. **View Available Stocks** - See all available stocks and their prices

### Advanced Features
- ✅ Input validation with comprehensive error handling
- ✅ Try-except blocks for exception handling
- ✅ Professional terminal UI with formatted tables
- ✅ Emoji indicators for visual feedback
- ✅ Timestamp-based file naming
- ✅ Type hints for better code documentation
- ✅ Modular function structure for maintainability

---

## 📦 Project Structure

```
StockPortfolioTracker/
│
├── src/
│   └── stock_portfolio_tracker.py       # Main application
│
├── data/                                 # Portfolio data storage
│   └── (portfolio files saved here)
│
├── requirements.txt                      # Python dependencies
├── README.md                             # This file
└── EXAMPLES.md                           # Example usage guide
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation & Setup

1. **Navigate to project directory:**
   ```bash
   cd StockPortfolioTracker
   ```

2. **Install optional dependencies (recommended):**
   ```bash
   pip install -r requirements.txt
   ```
   
   > **Note:** The application works without these dependencies. They're optional for enhanced features.

### Running the Application

```bash
python src/stock_portfolio_tracker.py
```

Or on Windows:
```bash
python src\stock_portfolio_tracker.py
```

---

## 📖 Usage Guide

### Menu Options Explained

#### 1️⃣ Add Stock to Portfolio
- Add new stocks or increase quantity of existing stocks
- Input validation for symbol and quantity
- Real-time feedback on additions
- Auto-converts symbols to uppercase

**Example:**
```
Enter stock symbol (e.g., AAPL): AAPL
Enter quantity for AAPL: 10
✅ Success! Added 10 shares of AAPL to portfolio
```

#### 2️⃣ View Portfolio
- Displays all holdings in a formatted table
- Shows: Symbol, Quantity, Price Per Share, Total Value
- Calculates and displays total portfolio value
- Stocks displayed in alphabetical order

**Example Output:**
```
Symbol       Quantity        Price/Share     Total Value    
─────────────────────────────────────────────────────────────
AAPL         10.00           $180.00         $1,800.00      
TSLA         5.00            $250.00         $1,250.00      
─────────────────────────────────────────────────────────────
TOTAL PORTFOLIO VALUE                        $3,050.00
```

#### 3️⃣ Remove Stock from Portfolio
- View current portfolio
- Select stock to remove with confirmation
- Prevents accidental deletions

#### 4️⃣ Calculate Portfolio Total
- Shows detailed portfolio statistics
- Displays percentage breakdown per stock
- Shows total shares and average price per share

**Example Output:**
```
AAPL: 10.00 shares × $180 = $1,800.00 (59.0%)
TSLA: 5.00 shares × $250 = $1,250.00 (41.0%)
─────────────────────────────────────────────────────────────
Total Shares: 15.00
Total Portfolio Value: $3,050.00
Average Price Per Share: $203.33
```

#### 5️⃣ Profit/Loss Simulation
- Compares previous prices with current prices
- Shows individual stock gains/losses
- Displays percentage change and profit/loss value
- Calculates total portfolio profit/loss

**Example Output:**
```
Symbol       Quantity     Prev Price   Curr Price   Change       P&L        
─────────────────────────────────────────────────────────────────────────
AAPL         10.00        $160.00      $180.00      +12.50%      📈   +$200.00
TSLA         5.00         $220.00      $250.00      +13.64%      📈   +$150.00
─────────────────────────────────────────────────────────────────────────
Total Profit/Loss:                                              📈 GAIN +$350.00
```

#### 6️⃣ Save Portfolio to CSV
- Exports portfolio data to CSV format
- Includes symbols, quantities, prices, and P&L
- Useful for analysis in Excel or other tools
- Auto-generated timestamp in filename

#### 7️⃣ Save Portfolio to TXT
- Exports portfolio to human-readable text format
- Includes portfolio details and profit/loss analysis
- Easy to read and print

#### 8️⃣ Load Portfolio from CSV
- Loads previously saved portfolios
- Lists available saved files
- Replaces current portfolio with loaded data

#### 9️⃣ Show Available Stocks & Prices
- Displays all available stocks
- Shows current and previous prices
- Shows price change percentage

#### 🔟 Exit
- Gracefully exits the application
- Shows goodbye message

---

## 💻 Code Features & Learning Points

### Python Concepts Covered

1. **Dictionaries**
   ```python
   CURRENT_STOCK_PRICES = {"AAPL": 180, "TSLA": 250, ...}
   portfolio = {}
   ```

2. **Type Hints**
   ```python
   def validate_quantity(quantity: str) -> Tuple[bool, Optional[float]]:
   ```

3. **Exception Handling**
   ```python
   try:
       qty = float(quantity)
       if qty > 0:
           return True, qty
   except ValueError:
       print("Invalid quantity!")
       return False, None
   ```

4. **Functions with Parameters and Return Values**
   ```python
   def add_stock() -> None:
       # Implementation
   ```

5. **Loops and Conditionals**
   ```python
   for symbol in portfolio:
       if symbol in CURRENT_STOCK_PRICES:
           # Process
   ```

6. **File Handling**
   ```python
   with open(filepath, 'w') as csvfile:
       writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
   ```

7. **String Formatting**
   ```python
   print(f"{symbol:<12} ${price:<14.2f}")
   ```

8. **Input Validation**
   ```python
   symbol = input("Enter symbol: ").upper().strip()
   if not validate_stock_symbol(symbol):
       return
   ```

---

## 📊 Available Stock Symbols

| Symbol | Current Price | Previous Price |
|--------|----------------|-----------------|
| AAPL   | $180          | $160           |
| TSLA   | $250          | $220           |
| GOOGL  | $140          | $130           |
| MSFT   | $330          | $300           |
| AMZN   | $145          | $135           |

---

## 🔄 Sample Workflow

### Example Session

```
1. Start Application
   → Opens main menu

2. Add AAPL
   → Enter: AAPL
   → Enter: 10 shares
   → Success! Portfolio now has 10 AAPL

3. Add TSLA
   → Enter: TSLA
   → Enter: 5 shares
   → Success! Portfolio now has 5 TSLA

4. View Portfolio
   → Shows formatted table with all holdings

5. Profit/Loss Simulation
   → Shows that AAPL gained $200, TSLA gained $150
   → Total gain: $350

6. Save to CSV
   → Saves as portfolio_20240526_143022.csv
   → File saved to data/ folder

7. Exit
   → Closes application
```

---

## 🎨 Optional Enhancements

### 1. Colorized Terminal Output (Using Colorama)

Install colorama:
```bash
pip install colorama
```

Add to your code:
```python
from colorama import Fore, Style

def add_color():
    print(f"{Fore.GREEN}✅ Success!{Style.RESET_ALL}")
    print(f"{Fore.RED}❌ Error!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}⚠️  Warning!{Style.RESET_ALL}")
```

### 2. Create Charts with Matplotlib

Install matplotlib:
```bash
pip install matplotlib
```

Create a pie chart of portfolio allocation:
```python
import matplotlib.pyplot as plt

def create_portfolio_chart():
    symbols = list(portfolio.keys())
    values = [portfolio[s] * CURRENT_STOCK_PRICES[s] for s in symbols]
    
    plt.pie(values, labels=symbols, autopct='%1.1f%%')
    plt.title('Portfolio Allocation')
    plt.show()
```

### 3. Advanced Data Analysis with Pandas

Install pandas:
```bash
pip install pandas`

Create portfolio analysis:
```python
import pandas as pd

def create_portfolio_df():
    data = {
        'Symbol': list(portfolio.keys()),
        'Quantity': list(portfolio.values()),
        'Price': [CURRENT_STOCK_PRICES[s] for s in portfolio],
    }
    df = pd.DataFrame(data)
    df['Total Value'] = df['Quantity'] * df['Price']
    return df
```

---

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'csv'"
**Solution:** The csv module is built-in. This error shouldn't occur. Make sure you're using Python 3.7+

### Issue: "Permission denied" when saving files
**Solution:** 
- Ensure you have write permissions in the project directory
- Create the 'data' folder manually if needed
- Run the application in a directory you have permissions for

### Issue: "Invalid stock symbol"
**Solution:** The application only supports: AAPL, TSLA, GOOGL, MSFT, AMZN
- Check the "Show Available Stocks" menu option
- Ensure you're typing the symbol in the correct case (auto-converted to uppercase)

### Issue: Negative quantity error
**Solution:** Quantities must be positive numbers. You cannot add negative shares.

---

## 📝 Code Comments & Documentation

Every function includes:
- **Docstrings** explaining purpose and parameters
- **Inline comments** for complex logic
- **Type hints** for parameters and return values
- **Error handling** with try-except blocks
- **User-friendly messages** for all operations

---

## 🎓 Learning Resources

This project demonstrates:
- ✅ Professional code structure
- ✅ Input validation and error handling
- ✅ Dictionary manipulation
- ✅ File I/O operations
- ✅ String formatting and alignment
- ✅ Type hints and documentation
- ✅ Function decomposition
- ✅ Menu-driven application design

---

## 📄 License & Usage

This project is provided as an educational tool for learning Python programming.

---

## 🚀 Future Enhancements

Potential improvements to extend the project:

1. **Database Integration**
   - Use SQLite for persistent storage
   - Support for multiple user accounts

2. **Real-time Stock Prices**
   - Integrate with stock APIs (Alpha Vantage, IEX Cloud)
   - Auto-update prices from the internet

3. **Advanced Analytics**
   - Portfolio performance charts
   - Historical price tracking
   - Buy/sell recommendations

4. **GUI Version**
   - Create a graphical user interface with tkinter or PyQt
   - Better visualization and user experience

5. **Multi-Currency Support**
   - Support for different currencies
   - Exchange rate conversion

6. **Portfolio Comparison**
   - Compare multiple portfolios
   - Track portfolio changes over time

7. **Risk Analysis**
   - Calculate portfolio risk metrics
   - Show beta and volatility

---

## 💡 Tips for Success

1. **Start Small** - Add 2-3 stocks first to understand the workflow
2. **Try All Features** - Explore each menu option to get familiar
3. **Save Your Work** - Use CSV export to preserve your portfolio
4. **Experiment** - Try different stock combinations
5. **Learn the Code** - Read through the source code to understand Python concepts
6. **Extend It** - Add your own features and enhancements

---

## 📞 Support & Questions

- Review the code comments for detailed explanations
- Check EXAMPLES.md for usage examples
- Refer to Python documentation for built-in modules

---

**Happy Investing! 📈💰**

