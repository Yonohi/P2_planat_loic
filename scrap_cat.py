import requests
from bs4 import BeautifulSoup
from scrap_livre import scraper

url_cat = "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
url_livres = []

"""Mettre les url des pages d'une categorie dans une liste"""
list_url_page = [url_cat]
response = requests.get(url_cat)
i = 2

while response.ok:
    url_test = url_cat.replace("index",f"page-{i}")
    response = requests.get(url_test)
    if response.ok:
        list_url_page.append(url_test)
    i+=1

"""On crée une boucle pour recuperer les url des livres de toutes les pages"""
for url_page in list_url_page:
    response = requests.get(url_page)
    soup = BeautifulSoup(response.text, features="html.parser")

    """Selection des livres d'une page"""
    list_info = soup.find("ol", {"class": "row"}).findAll("h3")
    for livre in list_info:
        url_livres.append("http://books.toscrape.com/catalogue"+livre.find("a")["href"].replace("../../..", ""))
    print(url_livres)

"""Ecriture dans le fichier"""
with open("info_livre.csv", "w") as file:
    file.write("product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url" + "\n")
    for url in url_livres :
        file.write(scraper(url))
#file.write(scraper("http://books.toscrape.com/catalogue/harry-potter-and-the-half-blood-prince-harry-potter-6_326/index.html"))
#il faudra surement que je redeplace le with open dans le scrap all et que je fasse de ce fichier une fonction qui me retournera la liste url_livres