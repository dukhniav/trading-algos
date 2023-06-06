from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from sentiment import analyze
from db import DB

options = Options()
options.add_argument("--headless")  # Opens the browser up in the background
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

db = DB()

stock_ticker = 'AAPL'

url = f"https://finance.yahoo.com/quote/{stock_ticker}/news"

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

# Find all the news articles on the page
articles = soup.find_all('h3', class_='Mb(5px)')

if len(articles) == 0:
    print("No news articles found for the stock ticker:", stock_ticker)

for article in articles:
    # Extract the headline and source of each news article
    headline = article.text

    for a in article.find_all('a', href=True):
        new_url = 'https://finance.yahoo.com' + a["href"]
        driver.get(new_url)
        soup2 = BeautifulSoup(driver.page_source, 'lxml')
        
        # Find the article title, date/time, and text on the page
        article_title = soup2.find("div", {"class": "caas-title-wrapper"}).text.strip()
        

        article_datetime = soup2.find('time').text.strip()
        article_text = soup2.find("div", {"class": "caas-body"}).text.strip()

        # print("Title:", article_title)
        # print("Date/Time:", article_datetime)
        # # print("Text:", article_text)
        sentiment = analyze(article_text)
        db.insert_sentiment(title=article_title, datetime=article_datetime, sentiment=sentiment['sentiment'], score_negative=sentiment['sentiment_neg'], score_neutral=sentiment['sentiment_neu'], score_positive=sentiment['sentiment_pos'], score_compound=sentiment['compound'])

driver.quit()

db.query_sentiment_results()