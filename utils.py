import sys
import os
import json
import pickle
from dotenv import load_dotenv
from typing import Any
import pandas as pd


class Utils:
	def __init__(self) -> None:
		self.config_path = 'config.json'
		self.alpha_vantage_api_key = None
		self.tickers = None

		self.setup()
		self.load_config()

	def setup(self):
		# Load env variables
		load_dotenv()

		# Load config variables
		self.alpha_vantage_api_key = os.getenv("ALPHA_VANTAGE_API_KEY", "")

	def load_config(self):
		with open(self.config_path, "r") as file:
			config = json.load(file)

		self.news_cutoff = config["old_news_day_cutoff"]
		self.tickers = config["tickers"]
