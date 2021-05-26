# P2_planat_loic 

Projet de scraping pour valider le P2 de la formation Developpeur Python.
Il s'agit ici de récupérer des informations sur des livres en vente sur le site Books to scrape et de les placer dans un fichier CSV
ainsi que les images des livres. Les données étant rangées par catégorie.
***

## Installation

Dans le Terminal, se déplacer dans le dossier censé accueillir le dépôt
grâce à la commande cd suivi du chemin du dossier:
```
cd <chemindossier>
```

Initialiser git:
```
git init
```

Cloner le dépôt distant:
```
git remote add origin https://github.com/Yonohi/P2_planat_loic.git
git clone https://github.com/Yonohi/P2_planat_loic.git
```
Créer l'environnement de développement et l'activer:
```
python3 -m venv env
source env/bin/activate
```

Installer les packages:
```
pip install -r requirements.txt
```
## Lancement du script
Toujour dans le Terminal:
```
python3 scrap_all.py
```

## Conclusion
Vous devriez voir apparaître un dossier **Info_recolte** contenant les dossiers des différentes catégories dans lesquel se trouve un **fichier CSV du même nom** et un dossier **Images**.




