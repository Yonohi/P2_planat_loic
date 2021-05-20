import requests
from bs4 import BeautifulSoup

"""Selection d'un url pour l'exemple"""
url = "http://books.toscrape.com/catalogue/harry-potter-and-the-half-blood-prince-harry-potter-6_326/index.html"


def scraper (url):
    """Recuperation de la reponse et du contenu"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")

    """Selection du titre en enlevant les sauts de ligne"""
    title = soup.find("title").text.replace("\n", "")
    print(title)

    """Selection de la zone d'information produit"""
    info_prod = soup.find("table", {"class": "table table-striped"}).findAll("td")
    upc = info_prod[0].text
    review_rating = info_prod[6].text
    # Cas particulier pour les prix
    price_including_tax = str(info_prod[2].text).replace("Â", "")
    price_excluding_tax = str(info_prod[3].text).replace("Â", "")
    # Cas particulier pour le nombre disponible
    availability = info_prod[5].text
    number_available = 0
    for char in availability:
        try:
            int(char)
            number_available = char
        except ValueError:
            pass
    print(number_available)
    print(price_excluding_tax)
    print(price_including_tax)
    print(review_rating)
    print(upc)

    """Selection de la description du livre en enlevant les caracteres indesirables"""
    zone_desc = soup.find("article", {"class": "product_page"}).findAll("p")
    product_description = zone_desc[3].text.replace("\"", "")
    print(product_description)

    """Selectionner la categorie"""
    breadcrumb = soup.find("ul", {"class": "breadcrumb"}).findAll("a")
    category = breadcrumb[2].text
    print(category)

    """Selectionner l'url de l'image"""
    info_img = soup.find("div", {"class": "item active"}).find("img")
    image_url = "http://books.toscrape.com"+info_img["src"].replace("../..", "")
    print(image_url)
    return (url + "," + upc + ",\"" + title + "\"," + price_including_tax + "," + price_excluding_tax + "," + number_available + ",\"" + product_description + "\"," + category + "," + review_rating + "," + image_url + "\n")
