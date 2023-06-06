import sqlite3

class DB:
	def __init__(self) -> None:
		# Step 1: Connect to the SQLite database
		self.conn = sqlite3.connect("sentiment_analysis.db")
		self.conn.row_factory = sqlite3.Row  # Enable accessing columns by name
		self.create_sentiment_table()

	def create_sentiment_table(self):
		self.conn.execute("""
			CREATE TABLE IF NOT EXISTS sentiment_results (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				ticker TEXT,
				title TEXT,
				datetime TEXT,
				sentiment TEXT,
				score_negative REAL,
				score_neutral REAL,
				score_positive REAL,
				score_compound REAL,
				CONSTRAINT unique_title_datetime UNIQUE (title, datetime)
			)
		""")

	def insert_sentiment(self, 
		      			ticker,
						title, 
						datetime, 
						sentiment, 
						score_negative,
						score_neutral,
						score_positive,
						score_compound):
		try:
			# Step 4: Insert the data into the table
			self.conn.execute("""
				INSERT INTO sentiment_results (ticker, title, datetime, sentiment, score_negative, score_neutral, score_positive, score_compound)
				VALUES (?, ?, ?, ?, ?, ?, ?, ?)
			""", (ticker, title, datetime, sentiment, score_negative, score_neutral, score_positive, score_compound))

			# Step 5: Commit the changes
			self.conn.commit()
		except sqlite3.IntegrityError:
			# Handle the integrity error for duplicate entry
			print("Duplicate entry. Skipping insertion.")

	def query_all_sentiment_results(self):
		cursor = self.conn.execute("SELECT * FROM sentiment_results")
		rows = cursor.fetchall()
		cursor.close()
		return 
	
	def print_all_sentiment_results(self):
		results = self.query_all_sentiment_results()
		# Iterate over the rows and print the data
		for row in results:
			print("Ticker:", row["ticker"])
			print("Title:", row["title"])
			print("Datetime:", row["datetime"])
			print("Sentiment:", row["sentiment"])
			print("Negative Score:", row["score_negative"])
			print("Neutral Score:", row["score_neutral"])
			print("Positive Score:", row["score_positive"])
			print("Compound Score:", row["score_compound"])
			print("------------------------------------")

	def close_connection(self):
		self.conn.close()
