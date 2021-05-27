# P2_planat_loic 

Scraping project to validate P2 from the formation Python Developer.
The goal is to collect some informations concerning books for sale on the website Books to scrape and to put them in a CSV file. The same thing should be done for the image of each book.
Datas are stored by category.
***

## Installation

In the terminal, move to the directory where you want to install the repository with the command line:
```
cd <pathdirectory>
```

Initialize git:
```
git init
```

Clone the remote repository:
```
git remote add origin https://github.com/Yonohi/P2_planat_loic.git
git clone https://github.com/Yonohi/P2_planat_loic.git
```
Move to the new folder:
```
cd P2_planat_loic
```

Create the development environment and activate it:
```
python3 -m venv env
source env/bin/activate
```

Install packages:
```
pip install -r requirements.txt
```
## Launch of the script:
In the terminal:
```
python3 scrap_all.py
```

## Conclusion
You should see a folder named **Info_recolte** which contains the folders of the different categories, themselves containing a **CSV file with the same name** and another folder named **Images**.




