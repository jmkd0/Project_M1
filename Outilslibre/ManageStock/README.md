# Project Mini Magasin - Outils scolaires 

### Projet outils libres pour developpement logiciel
#### Application desktop Python pour gérer les produits et les achats de manière interactive via la console

L'objectif de ce travail pratique est de créer un programme de gestion des achats pour tester l'accès aux données et les
enregistrer dans un format à l'aide de différents outils libres.

Programme qui vous permet de contrôler les ventes d'un supermarché, ainsi que l'entrée dans l'entrepôt de celui-ci.

Chaque produit est identifié par un nom, une quantité en stock et un prix.

Le magasin vend 10 types de produits différents qui sont: cahier, stylo, gomme, crayon ciseaux, compas, surligneurs,
 equerre et rapporteur. Chaque produit est vendu individuellement.
  
Le programme utilise le paradigme de la programmation orientée objet en Python et répond aux exigences suivantes:

1. Ajouter un produit au magasin
2. Modifier l'existence du produit
3. Afficher les produits
4. Rapport de produits en faible stock
5. Obtenez un design flexible

#### Présentation du projet

1. [Structure du programme](#1)
2. [Avant de commencer](#2)
3. [Création de bases de données et de tables](#3)
4. [Fonctionnement](#4)


### <a name="1"></a> Structure du programme

xxx

##### Persistance des données

L'application utilise deux méthodes de persistance des données.

* Une base de données SQLite dans laquelle se trouve une table: MAGASIN. Grâce aux fonctions implémentées dans le fichier controller.py, nous pouvons gérer les informations. La base de données et les informations qu'elle contient seront conservées même si nous terminons l'exécution du programme.

* Fichiers texte .TXT où sont stockées les informations de l'achat à effectuer et qui sont exécutées lors de la sélection de «Charge Receipt et puis Validate.


### <a name="2"></a>Avant de commencer

Pour exécuter l'application, la première chose que vous devez installer sur votre système est Python. Vous pouvez installer la dernière version via:

* [Télécharger à partir du Web Python]( https://www.python.org/downloads/).

L'étape suivante consiste à télécharger les fichiers depuis ce répertoire ou par la console. Pour cela, vous avez besoin du code suivant:

```sh
~$ sudo apt-get install git
~$ git clone https://github.com/Sarouule/ProjetGestionDeStock.git
```
### <a name="3"></a>Création de la base de données et de la table

Les fichiers de ce répertoire incluent un fichier .SQL avec les scripts pour créer la table MAGASIN requise dans la base de données, avec les champs, types de données et restrictions respectifs. Le code est le suivant:

```sql
create table "magasin" ( 
cle INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
produit NVARCHAR(160)  NOT NULL,
quantite INTEGER  NOT NULL,
prix FLOAT  NOT NULL
)
```

### <a name="4"></a>Fonctionnement

Pour exécuter l'application, la base de données doit être chargée. Cela peut être fait directement à partir de la console de l'éditeur de code utilisé.

``` sh
~ / < > ProjetGestionDeStock $ python initDB.py
~ / < > ProjetGestionDeStock $ python frontend.py
```

Lorsque l'application est exécutée, le menu principal apparaîtra sur la console, offrant à l'utilisateur cinq options

1. Display articles.
2. Charge receipt.
3. Search.
4. Add or update.

![Menu](1_Menu.png)


##### Display articles

Ici vous pouvez voir le stock de produits dans le magasin. S'il n'y a pas de produits, logiquement, vous ne pouvez pas acheter. On peut voir son nom, sa quantité et son prix.

![Display](2_Display.png)

##### Charge receipt

Vous pouvez charger le reçu d'achat du client .txt qui contient le nom du produit et la quantité, cela permet la validation respective et la réduction du montant du stock du magasin.

Si le produit en stock est inférieur à 10, le système affichera une notification disant " Attention, le produit « Regle » est bientot epuisé"" et s'il n'y a pas de produit en stock " "Attention, le produit « Cahier » est epuisé""

![charger](3_charger.png)

##### Search et Add or update

Vous pouvez rechercher un article pour connaître la quantité existante et son prix ou vous pouvez également ajouter une nouvelle quantité au stock et modifier son prix, ces informations seront ajoutées ou modifiées dans la base de données.

Si vous recherchez un article qui n'existe pas dans la base de données, une notification vous avertira “Not exist but you can add as new...”

Le nom est unique et ne peut pas être répété ou doit être modifié, seuls la quantité et le prix peuvent être modifiés. “Not exist but you can add as new...” 

![search](4_search.png)
 

Dans le lien suivant [Project demo Stock]( https://jmkd.fr/projects_demos/project_manage_stock.mp4), vous pouvez voir comment fonctionne le mini-magasin

**Versión 0.1.0**

* Principales fonctionnalités de l'application: affichage des produits, modification et achat.
* Persistance des données: base de données pour stocker les produits; Fichier .TXT pour stocker les reçus (toujours avec le même nom "products.txt"


