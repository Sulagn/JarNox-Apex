import yfinance as yf

def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        # 5 days of hourly data
        hist = stock.history(period="5d", interval="1h")
        
        if hist.empty:
            return {"error": f"No data found for ticker: {ticker}"}
        
        # Convert last 5 rows to JSON-serializable format
        return hist.tail(5).reset_index().to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
