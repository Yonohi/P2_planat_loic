import requests
from bs4 import BeautifulSoup


url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
list_url = [url]
response = requests.get(url)
i = 2

while response.ok:
    url_test = url.replace("index",f"page-{i}")
    response = requests.get(url_test)
    if response.ok:
        list_url.append(url_test)
    i+=1
    print(list_url)