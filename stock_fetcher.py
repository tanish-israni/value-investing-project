import yfinance as yf
import pandas as pd
from datetime import datetime
import time

def fetch_data():
    print(f"[{datetime.now()}] Fetching stock data (with price)...")
    df = pd.read_csv('ind_nifty500list.csv')
    symbols = df['Symbol'].tolist()
    symbols = [s + '.NS' for s in symbols]

    stock_data = []

    for symbol in symbols:
        try:
            print(f"[{datetime.now()}] Fetching data for {symbol}...")
            stock = yf.Ticker(symbol)
            info = stock.info
            data = {
                "stock": symbol,
                "current_price": info.get("currentPrice"),
                "p_e_ratio": info.get("trailingPE"),
                "p_b_ratio": info.get("priceToBook"),
                "p_s_ratio": info.get("priceToSalesTrailing12Months"),
                "ev_ebitda": info.get("enterpriseToEbitda"),
                "ev_gp": info.get("grossProfits")
            }
            stock_data.append(data)
            time.sleep(1)  # Be mindful of rate limiting
        except Exception as e:
            print(f"[{symbol}] Error: {e}")
            continue

    df_final = pd.DataFrame(stock_data)
    df_final.to_csv('nifty500_fundamental.csv', index=False)
    print(f"[{datetime.now()}] Data update (with price) completed. CSV saved.")

if __name__ == '__main__':
    fetch_data()