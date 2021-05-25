import requests
from bs4 import BeautifulSoup
import re


def scraper(url, folder):
    """Scrape the following information : upc, title, price_including_tax, price_excluding_tax, number_available,
    product_description, category, review_rating, image_url

    :param url: web page to scrape
    :param folder:
    :return: A string with the wanted information
    """
    # Recuperation de la reponse et du contenu, en changeant l'encodage pour les caracteres speciaux
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, features="html.parser")

    # Selection du titre en enlevant les sauts de ligne
    title = soup.find("title").text.replace("\n", "").strip()

    # Selection du nombre d'etoiles
    star_number = soup.find("div", {"class": "col-sm-6 product_main"}).findAll("p")[2]["class"][1]
    dict_star = {"One": "1/5", "Two": "2/5", "Three": "3/5", "Four": "4/5", "Five": "5/5"}
    review_rating = dict_star[star_number]

    # Selection de la zone d'information produit
    info_prod = soup.find("table", {"class": "table table-striped"}).findAll("td")
    upc = info_prod[0].text
    # review_rating = info_prod[6].text
    # Cas particulier pour les prix
    price_including_tax = str(info_prod[2].text)  # .replace("Â", "")
    price_excluding_tax = str(info_prod[3].text)  # .replace("Â", "")
    # Cas particulier pour le nombre disponible
    availability = info_prod[5].text
    number_available = re.sub("[a-zA-Z() ]", "", availability)
    if number_available == "":
        number_available = 0
    else:
        number_available = int(number_available)

    # Selection de la description du livre en enlevant les caracteres indesirables
    zone_desc = soup.find("article", {"class": "product_page"}).findAll("p")
    product_description = zone_desc[3].text.replace("\"", "").strip()

    # Selectionner la categorie
    breadcrumb = soup.find("ul", {"class": "breadcrumb"}).findAll("a")
    category = breadcrumb[2].text

    # Selectionner l'url de l'image
    info_img = soup.find("div", {"class": "item active"}).find("img")
    image_url = "http://books.toscrape.com"+info_img["src"].replace("../..", "")

    # Enregistrement de l'image dans le dossier souhaite en enlevant les caracteres problematiques
    title_inter = re.sub("[.,;/:<\">+*!?()|=]", "", title)
    title_img = re.sub(" ", "_", title_inter)
    with open(f"Info_recolte/{folder}/Images/{title_img}.jpg", "wb") as img:
        img.write(requests.get(image_url).content)

    # On renvoi les informations voulues
    return (url + ","
            + upc + ",\""
            + title + "\","
            + price_including_tax + ","
            + price_excluding_tax + ","
            + str(number_available) + ",\""
            + product_description + "\","
            + category + ","
            + review_rating + ","
            + image_url + "\n")
