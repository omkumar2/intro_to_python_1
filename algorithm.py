import yfinance as yf
import pandas as pd

# Download historical data
data = yf.download("AAPL", start="2023-01-01", end="2024-01-01")

# Calculate moving averages
data["SMA20"] = data["Close"].rolling(window=20).mean()
data["SMA50"] = data["Close"].rolling(window=50).mean()

# Generate trading signals
data["Signal"] = 0
data.loc[data["SMA20"] > data["SMA50"], "Signal"] = 1  # Buy
data.loc[data["SMA20"] < data["SMA50"], "Signal"] = -1 # Sell

print(data[["Close", "SMA20", "SMA50", "Signal"]].tail())
