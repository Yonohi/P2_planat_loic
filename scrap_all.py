import requests
from bs4 import BeautifulSoup
from scrap_cat import scraper_cat

# Url to scrape
url = "http://books.toscrape.com"

# Retrieving source code
response = requests.get(url)
soup = BeautifulSoup(response.text, features="html.parser")

# Retrieving categories
list_cat = soup.find("ul", {"class": "nav nav-list"}).findAll("a")[1:]

# Generating url and start scraping
for cat in list_cat:
    url_cat = "http://books.toscrape.com/"+cat["href"]
    categorie = cat.text.strip().replace(" ", "_")
    scraper_cat(url_cat, categorie)
    print(str(categorie) + " finie")
