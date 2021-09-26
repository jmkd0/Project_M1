import sqlite3
conn = sqlite3.connect('my.db')
cur = conn.cursor()


cur.execute("create table IF NOT EXISTS magasin ( cle INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
produit NVARCHAR(160)  NOT NULL, \
quantite INTEGER  NOT NULL, \
prix FLOAT  NOT NULL)")

cur.execute("INSERT INTO magasin (produit, quantite, prix ) VALUES('CAHIER',100, 1.9)")

cur.execute("INSERT INTO magasin (produit, quantite, prix ) VALUES('STYLO',100, 1.2)")

cur.execute("INSERT INTO magasin (produit, quantite, prix ) VALUES('GOMME',10, 1.3)")

cur.execute("INSERT INTO magasin (produit, quantite, prix ) VALUES('CRAYON',100, 1.5)")

cur.execute("INSERT INTO magasin (produit, quantite, prix ) VALUES('CISEAUX',100, 1.6)")

cur.execute("INSERT INTO magasin (produit, quantite, prix ) VALUES('COMPAS',100, 1.7)")

cur.execute("INSERT INTO magasin (produit, quantite, prix ) VALUES('SURLIGNEURS',100, 2.2)")

cur.execute("INSERT INTO magasin (produit, quantite, prix ) VALUES('REGLE',100, 1.1)")

cur.execute("INSERT INTO magasin (produit, quantite, prix ) VALUES('EQUERRE',100, 1.2)")

cur.execute("INSERT INTO magasin (produit, quantite, prix ) VALUES('RAPPORTEUR',100, 1.5)")
conn.commit()
cur.close