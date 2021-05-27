import requests
from bs4 import BeautifulSoup
import re


def scraper(url, folder):
    """Scrape the following informations : upc, title, price_including_tax, price_excluding_tax, number_available,
    product_description, category, review_rating, image_url

    :param url: The web page to scrape
    :param folder: The name of the folder which will contain the CSV file and the folder named Images.
    :return: A string with the wanted information
    """
    # Retrieving of response and content, changing the encoding for special characters
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, features="html.parser")

    # Title selection by removing line breaks
    title = soup.find("title").text.replace("\n", "").strip()

    # Selection of the number of stars
    star_number = soup.find("div", {"class": "col-sm-6 product_main"}).findAll("p")[2]["class"][1]
    dict_star = {"One": "1/5", "Two": "2/5", "Three": "3/5", "Four": "4/5", "Five": "5/5"}
    review_rating = dict_star[star_number]

    # Selection of the product information area
    info_prod = soup.find("table", {"class": "table table-striped"}).findAll("td")
    upc = info_prod[0].text
    
    # Special case for prices
    price_including_tax = str(info_prod[2].text) 
    price_excluding_tax = str(info_prod[3].text) 
    
    # Special case for the number available
    availability = info_prod[5].text
    number_available = re.sub("[a-zA-Z() ]", "", availability)
    if number_available == "":
        number_available = 0
    else:
        number_available = int(number_available)

    # Selection of the description of the book by removing unwanted characters
    zone_desc = soup.find("article", {"class": "product_page"}).findAll("p")
    product_description = zone_desc[3].text.replace("\"", "").strip()

    # Category selection
    breadcrumb = soup.find("ul", {"class": "breadcrumb"}).findAll("a")
    category = breadcrumb[2].text

    # Selection of the image url
    info_img = soup.find("div", {"class": "item active"}).find("img")
    image_url = "http://books.toscrape.com"+info_img["src"].replace("../..", "")

    # Save the image in the desired folder by removing the problematic characters
    title_inter = re.sub("[.,;/:<\">+*!?()|=]", "", title)
    title_img = re.sub(" ", "_", title_inter)
    with open(f"Info_recolte/{folder}/Images/{title_img}.jpg", "wb") as img:
        img.write(requests.get(image_url).content)

    # Return of the desired information
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
