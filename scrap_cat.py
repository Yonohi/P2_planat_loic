import requests
from bs4 import BeautifulSoup
from scrap_book import scraper
import os


def scraper_cat(url_cat, categorie="erreur"):
    """Function calling the scraper from scrap_book and applying it for a category.
    
    :param url_cat: Url of the wanted category
    :param categorie: Name of the category
    """
    # Making of directory
    os.makedirs("Info_recolte", exist_ok=True)
    os.makedirs(f"Info_recolte/{categorie}", exist_ok=True)
    os.makedirs(f"Info_recolte/{categorie}/Images", exist_ok=True)

    # Writing in the CSV file
    with open(f"Info_recolte/{categorie}/{categorie}.csv", "w") as file:
        file.write("product_page_url,\
            universal_product_code,\
             title,\
              price_including_tax,\
               price_excluding_tax,\
                number_available,\
                 product_description,\
                  category,\
                   review_rating,\
                    image_url" + "\n")

        # Put the pages's url of a category in a list
        list_url_page = [url_cat]
        for url_page in list_url_page:
            response = requests.get(url_page)
            soup = BeautifulSoup(response.text, features="html.parser")
            # Selection of books in a page
            list_info = soup.find("ol", {"class": "row"}).findAll("h3")
            for livre in list_info:
                url_livre = "http://books.toscrape.com/catalogue" + livre.find("a")["href"].replace("../../..", "")
                # Writing the collected data in the csv file
                file.write(scraper(url_livre, categorie))
            # Test if a following page exists
            try:
                next_page = soup.find("li", {"class": "next"}).find("a")
                url_test = url_cat.replace("index.html", next_page["href"])
                list_url_page.append(url_test)
            except:
                pass
