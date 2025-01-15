import yfinance as yf
from django.http import JsonResponse

def is_valid_ticker(symbol):
    """Simple check if a ticker exists"""
    try:
        ticker = yf.Ticker(symbol)
        # Quick check - if we can get the info dict and it has a name, it's valid
        return bool(ticker.info.get('shortName'))
    except:
        return False 