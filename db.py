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
                title TEXT,
                datetime TEXT,
                sentiment TEXT,
                score_negative REAL,
                score_neutral REAL,
                score_positive REAL,
                score_compound REAL
            )
        """)

    def insert_sentiment(self, 
                         title, 
                         datetime, 
                         sentiment, 
                         score_negative,
                         score_neutral,
                         score_positive,
                         score_compound):
        # Step 4: Insert the data into the table
        self.conn.execute("""
            INSERT INTO sentiment_results (title, datetime, sentiment, score_negative, score_neutral, score_positive, score_compound)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (title, datetime, sentiment, score_negative, score_neutral, score_positive, score_compound))

        # Step 5: Commit the changes and close the connection
        self.conn.commit()

    def query_sentiment_results(self):
        cursor = self.conn.execute("SELECT * FROM sentiment_results")
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def close_connection(self):
        self.conn.close()
