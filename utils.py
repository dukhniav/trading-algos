import sys
import os
import json
import pickle
from dotenv import load_dotenv
from typing import Any
import pandas as pd


class Utils:
    def __init__(self) -> None:
        self.alpha_vantage_api_key = None
        self.tickers = None

    def setup(self):
        # Load env variables
        load_dotenv()

        # Load config
        f = open("config.json")
        config = json.load(f)
        f.close()

        # Load config variables
        self.alpha_vantage_api_key = os.getenv("ALPHA_VANTAGE_API_KEY", "")

        # Access the configuration settings
        db_name = config["database"]["name"]
        db_path = config["database"]["path"]
        api_key = config["api_key"]
        other_setting = config["other_setting"]
        tickers = config["tickers"]
