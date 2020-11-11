# -*- coding:Utf-8 -*-

import re
import sqlite3
conn = sqlite3.connect('my.db')
cur = conn.cursor()

#*********************** OUVERTURE DU FICHIER PRODUITS.TXT ET LECTURE DU CONTENU ************************

#Initialisation d'une liste vide de produits
listOfProducts = []
#--Ouverture du fichier en lecture
def openingFile(path):
    #file = open('products.txt',"r")
    file = open(path,"r")
    lines = file.readlines()
    listOfProductsTmp = []
    for line in lines:
    #Enlever l'espace et le \n de ma chaine de caractères
        line = re.split(' |\n',line) 
    #Supprimer les '' de la liste
        if '' in line:
            line.remove('')
    #Concatenation des deux chaines
        listOfProductsTmp += line
    print(listOfProductsTmp)
    file.close() 
    return listOfProductsTmp
   
    
#************************* GESTION DE LA BASE DE DONNEES *************************************************
#Les produits achetés dans le fichier "produits.txt" devront être écris sous la forme: PRODUIT QUANTITE(int)

#--Affichage de la base de données
def displayBDD():
    conn = sqlite3.connect('my.db')
    cur = conn.cursor()
    querry = "SELECT * FROM magasin"
    magasinTable = cur.execute(querry).fetchall()
    #print(magasinTable)
    return magasinTable
#--Modification de la base de données (décrementation des produits achetés)
def updateBDD(listOfProducts):
    #listOfProducts = openingFile()  
    with conn:
        querry = "SELECT * FROM magasin"
        magasinTable = cur.execute(querry).fetchall()
    #Parcours de la liste récuperée du fichier
        for i in range (len(listOfProducts)):
    #Parcous des lignes de la table "magasin"
            for line in magasinTable :
                if listOfProducts[i] in line:
    #Initialisation de la nouvelle variable représentant la nouvelle quantité du produit après achat
                    newqty = line[2] - int(listOfProducts[i+1])
                    if newqty < 0:
                        newqty = 0
                    cur.execute("""UPDATE magasin SET quantite = :quantity
                    WHERE produit = :product""", {'quantity':newqty, 'product':line[1]})

#--Remplissage du stock pour chaque produit
def fillStock(product):
    with conn:
        cur.execute("SELECT * FROM magasin WHERE produit = ?", (product[0],))
        magasinTable = cur.fetchone()
        if int(product[1]) < 0:
            product[1] = 0
        if magasinTable is not None:
            product[1] += magasinTable[2] 
            cur.execute("UPDATE magasin SET quantite = ?, prix = ? WHERE produit = ?", (product[1], product[2], product[0]))
        else:
            cur.execute("INSERT INTO magasin VALUES (NULL, ?,?,?)",(product[0], product[1], product[2]))


#--Envoie d'une notification si le stock d'un produit est inférieur à 20
def notifyEmptyStock():
    with conn:
        article_empty = []
        querry = "SELECT * FROM magasin"
        magasinTable = cur.execute(querry).fetchall()
        for line in magasinTable :
            if line[2] == 0:
                article_empty.append("Attention, le produit " + line[1] + " est epuisé")
            if line[2] >= 1 and line[2] <= 10:
                article_empty.append("Attention, le produit " + line[1] + " est bientot epuisé")
    return article_empty

#Recherche d'un article
def searchArticle(product):
    with conn:
        cur.execute("SELECT * FROM magasin WHERE produit = ?", (product,))
        magasinTable = cur.fetchall()
        return magasinTable

#************************* APPELS DES FONCTIONS **********************************************************

#Appel de la fonction de mise à jour de la BDD
#displayBDD()
#print("\n")
#updateBDD()
#print("\n")
#Affichage de la nouvelle table 
#displayBDD()
