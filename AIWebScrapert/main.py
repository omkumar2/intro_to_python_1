import pandas as pd
import yfinance as yf

# Fetch data
stock = yf.download("AAPL", start="2024-01-01", end="2025-04-04")
stock['MA50'] = stock['Close'].rolling(window=50).mean()
stock['MA200'] = stock['Close'].rolling(window=200).mean()

# Trading logic
if stock['MA50'].iloc[-1] > stock['MA200'].iloc[-1]:
    print("Buy signal!")
else:
    print("Sell or hold.")
    
    
    