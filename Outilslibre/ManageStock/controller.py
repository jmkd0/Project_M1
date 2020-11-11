import tkinter # conda install -c anaconda tk
from tkinter import filedialog
import main

receipt = None
def get_all_products(window, label_desc, label_rupture, entry_rupture):
    names = ["Number  ", " Product Name ", "    Quantity     ", "   Price    "]
    products = main.displayBDD()
    #display all products
    display_datas(window, label_desc, products, names)
    #Dispplay articles almost empty
    rupture_info = main.notifyEmptyStock()
    display_rupture(rupture_info, label_rupture, entry_rupture)
    
                #print(products)
def charge_data_from_file(window, label_desc):
    global receipt
    names = [" Product Name ", "    Number     "]
    path = tkinter.filedialog.askopenfilename(parent=window, title='Please select a directory')
    receipt = main.openingFile(path)
    receipts = []
    for i in range(0,len(receipt),2):
        receipts.append([receipt[i], receipt[i+1]])
    #display receipt articles
    display_datas(window, label_desc, receipts, names)
    

def update_data_by_receipt(window, label, label_rupture, entry_rupture):
    for widget in label.winfo_children():
            widget.destroy()
    if receipt is not None:
        main.updateBDD(receipt)
        get_all_products(window, label, label_rupture, entry_rupture)
        #Dispplay articles almost empty
        rupture_info = main.notifyEmptyStock()
        display_rupture(rupture_info, label_rupture, entry_rupture)
    
def search_product(window, article_name, entry_quantity, entry_price):
    name = article_name.get()
    product = main.searchArticle(name)
    if len(product) == 0:
        label = tkinter.Label(window, text="Not exist but you can add as new...", font=("helvetica", 15, "bold"), bg="white", fg="red", borderwidth=5)
        label.place(relx=0.75, rely=0.3)
        window.after(2000, label.destroy) 
        product = [[0,'',0,0]]
    entry_quantity.delete(0, tkinter.END)
    entry_price.delete(0, tkinter.END)
    entry_quantity.insert(0,product[0][2])
    entry_price.insert(0,product[0][3])

def add_or_update(window, label, entry_article_name, entry_quantity, entry_price, label_rupture, entry_rupture):
    article_name = entry_article_name.get()
    quantity = entry_quantity.get()
    price = entry_price.get()
    product = [article_name, int(quantity), float(price)]
    main.fillStock(product)
    get_all_products(window, label, label_rupture, entry_rupture)
    #Dispplay articles almost empty
    rupture_info = main.notifyEmptyStock()
    display_rupture(rupture_info, label_rupture, entry_rupture)


def display_datas(window, label, products, names):
    if len(products) == 0:
        label = tkinter.Label(window, text="No product is present", font=("helvetica", 15, "bold"), bg="white", fg="red", borderwidth=5)
        label.place(relx=0.25, rely=0.43)
        window.after(2000, label.destroy) 
    else:
        products.insert(0,names)
        erease_label(label)

        for i in range(len(products)): #Rows
            for j in range(len(products[0])):
                if i == 0:
                    b = tkinter.Label(label, text=products[i][j], font=("Times New Roman", 12, "bold"), bg="#0066CC", fg="white", borderwidth=4)
                elif i > 0 and j==3:
                    b = tkinter.Label(label, text=str(products[i][j])+"€", font=("Times New Roman", 11, "bold"), bg="#ECF5FF", fg="#272727", borderwidth=2)
                else:
                    b = tkinter.Label(label, text=products[i][j], font=("Times New Roman", 11, "bold"), bg="#ECF5FF",borderwidth=2)

                b.grid(row=i, column=j)

def display_rupture(rupture_info, label_rupture, entry_rupture):
    label_rupture.config(text = "")
    erease_label(entry_rupture)
    if len(rupture_info) > 0:
        label_rupture.config(text = "Notifications...")
        for i in range(len(rupture_info)):
            b = tkinter.Label(entry_rupture, text=rupture_info[i], font=("Times New Roman", 11, "bold"), fg="#796400", borderwidth=2)
            b.grid(row=i, column=0)

def erease_label(label):
    for widget in label.winfo_children():
            widget.destroy()

