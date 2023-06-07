import json
from yahoo_news import get_updates
from utils import Utils

def get_news_updates(tickers):
    for ticker in tickers:
        get_updates(ticker)

def main():
    # Load the configuration file
    utils = Utils()
    
    tickers = utils.tickers

    # Get updates on tickers
    get_news_updates(tickers)


if __name__ == "__main__":
    main()
