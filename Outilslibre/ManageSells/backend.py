import psycopg2 #conda install -c anaconda psycopg2    (postgres DataBase)
import datetime 
con = psycopg2.connect(
    host     = "localhost",
    database = "stockdata",
    user     = "komlan",
    password = "dakomaje00"
)


def create_account(name, identifier, password, category):
    cur = con.cursor()
    cur.execute("INSERT INTO users(username, identifier, password, category) VALUES (%s,%s,%s,%s)",(name, identifier, password, category))
    con.commit()
    #con.close()

def connexion(identifier, password):
    cur = con.cursor()
    cur.execute("SELECT identifier, password, category from users WHERE identifier=%s AND password=%s", (identifier, password))
    raws = cur.fetchall()
    con.commit()
    return raws

def get_product(product, quantity):
    cur = con.cursor()
    cur.execute("SELECT quantity, product_name, unit_sels_price from products WHERE product_name=%s", (product,))
    raws = cur.fetchall()
    if len(raws) == 0:
        return "neant"
    prod = list(raws[0])
    if prod[0] < 4: #alert de stock au seuil
        return "alert"
    if prod[0] > int(quantity):
        prod[0] = int(quantity)
    prod.append(int(prod[0])*prod[2])
    return prod

def save_sels(client_name, products):
    cur = con.cursor()
    date = datetime.datetime.now()
    for product in products:
        cur.execute("SELECT quantity from products WHERE product_name=?", (product[1]))
        raws = cur.fetchall()
        remain = raws[0][0]-product[0]
        cur.execute("UPDATE products SET quantity=?",(remain))
        cur.execute("INSERT INTO products_sels VALUES (NULL, ?,?,?,?,?)",(date, client_name, product[0], product[1], product[2])) #(date, Komlan, 4, stylo, 5€)
    con.commit()
    #con.close()

def search_product(product):
    cur = con.cursor()
    cur.execute("SELECT product_name ,quantity, unit_purchase_price, unit_sels_price from products WHERE product_name=%s", (product,))
    raws = cur.fetchall()
    con.commit() 
    #con.close()
    return raws

def add_new_or_update_product(article_name, stock_quantity, unit_purchase_price, unit_sels_price):
    cur = con.cursor()
    date = datetime.datetime.now()
    cur.execute("SELECT product_name from products WHERE product_name=%s", (article_name,))
    raws = cur.fetchall()
    if len(raws) == 0:
        cur.execute("INSERT INTO products(product_name ,quantity, unit_purchase_price, unit_sels_price, date) VALUES (%s, %s, %s, %s, %s)",(article_name, int(stock_quantity), int(unit_purchase_price), int(unit_sels_price), date)) 
    else:
        cur.execute("UPDATE products SET product_name=%s, quantity=%s, unit_purchase_price=%s, unit_sels_price=%s",(article_name, int(stock_quantity), int(unit_purchase_price), int(unit_sels_price)))
    con.commit()
    #con.close()

def search_client(client):
    cur = con.cursor()
    cur.execute("SELECT * from products_sels WHERE client_name=?", (client))
    raws = cur.fetchall()
    con.commit() 
    con.close()
    return raws
#for raw in raws:
#    print("id {raw[0]} name {raw[1]} ")

"""
CREATE TABLE users (
    id  serial primary key,
    username varchar not null,
    identifier varchar not null,
    password varchar not null,
    category varchar not null
);
CREATE TABLE products (
    id serial primary key,
    product_name varchar not null,
    quantity int not null,
    unit_purchase_price int not null,
    unit_sels_price int not null,
    date timestamp not null
);
CREATE TABLE products_sels (
    id serial primary key,
    date timestamp not null,
    client_name varchar,
    quantity int not null,
    product_name varchar not null,
    unit_sels_price int not null
);
"""
