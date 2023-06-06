import json
from yahoo_news import get_updates


def load_config(file_path):
    with open(file_path, "r") as file:
        config = json.load(file)
    return config


def get_news_updates(tickers):
    for ticker in tickers:
        get_updates(ticker)


def main():
    # Load the configuration file
    config = load_config("config.json")

    # Access the configuration settings
    db_name = config["database"]["name"]
    db_path = config["database"]["path"]
    api_key = config["api_key"]
    other_setting = config["other_setting"]
    tickers = config["tickers"]

    # Get updates on tickers
    get_news_updates(tickers)


if __name__ == "__main__":
    main()
