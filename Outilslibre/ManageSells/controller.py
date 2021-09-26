import tkinter # conda install -c anaconda tk
import frontend
import backend

global products
products = [["Quantity    ", " Product Name ", "    Unit Price     ", "   Total Price    "],["","","",0]]

def create_account(window, name, identifier, password, conf_pass, category):
    name = name.get()
    identifier = identifier.get()
    password   = password.get()
    conf_pass  = conf_pass.get()
    category   = category.get()
    if password !="" and conf_pass !="" and password == conf_pass:
        backend.create_account(name, identifier, password, category)
        label = tkinter.Label(window, text="You can now connect...", font=("helvetica", 15, "bold"), bg="white", fg="#00BB00", borderwidth=5)
        label.place(relx=0.55, rely=0.7)
        window.after(2000, label.destroy) 
    else:
        print("Please verify your password")


def connexion(window, identifier, password):
    identifier = identifier.get()
    password   = password.get()
    raws = backend.connexion(identifier, password)
    if len(raws) == 0:
        label = tkinter.Label(window, text="You don't have an account...", font=("helvetica", 15, "bold"), bg="white", fg="red", borderwidth=5)
        label.place(relx=0.35, rely=0.8)
        window.after(2000, label.destroy) 
    else:
        if raws[0][2] == "Caissier":
            frontend.manage_checkout(window)
        elif raws[0][2] == "Manager":
            frontend.manage_product_and_client(window)
        else:
            print("Error")

def search_product(window, product):
    product = product.get()
    raws = backend.search_product(product)
    if len(raws) == 0:
        raws = [product, 0, 0, 0]
    else:
        raws = raws[0]
    frontend.update_or_add_product(window, raws)

def update_or_add_product(window, article_name, stock_quantity, unit_purchase_price, unit_sels_price):
    name = article_name.get()
    quantity = stock_quantity.get()
    unit_purchase_price = unit_purchase_price.get()
    unit_sels_price = unit_sels_price.get()
    backend.add_new_or_update_product(name, quantity, unit_purchase_price, unit_sels_price)
    label = tkinter.Label(window, text="Your product is add successfuly...", font=("helvetica", 15, "bold"), bg="white", fg="#00BB00", borderwidth=5)
    label.place(relx=0.55, rely=0.7)
    window.after(2000, label.destroy) 

def get_product(window, label_desc, entry_article_name, entry_quantity):
    name = entry_article_name.get()
    quantity = entry_quantity.get()
    product = backend.get_product(name, quantity)
    if product == "neant":
        label = tkinter.Label(window, text="Unknown product", font=("helvetica", 15, "bold"), bg="white", fg="red", borderwidth=5)
        label.place(relx=0.25, rely=0.43)
        window.after(2000, label.destroy) 
    elif product == "alert":
        label = tkinter.Label(window, text="Remain few product", font=("helvetica", 15, "bold"), bg="white", fg="red", borderwidth=5)
        label.place(relx=0.25, rely=0.43)
        window.after(2000, label.destroy) 
    else:
        total = products[-1][3] #get the latest total
        del products[-1]    #delete the last line

        products.append(product) #add the new article
        total += product[3]     #add the new total
        products.append(["Total","","",total])

        for i in range(1, len(products)):
            products[i][2] = products[i][2]
            products[i][3] = products[i][3]

        for widget in label_desc.winfo_children():
            widget.destroy()

        for i in range(len(products)): #Rows
            for j in range(len(products[0])):
                if i == 0:
                    b = tkinter.Label(label_desc, text=products[i][j], font=("Times New Roman", 12, "bold"), bg="#0066CC", fg="white", borderwidth=4)
                elif i == len(products)-1 and j==0:
                    b = tkinter.Label(label_desc, text=products[i][j], font=("Times New Roman", 12, "bold"), bg="black", fg="white", borderwidth=4)
                elif i == len(products)-1 and j==len(products[0])-1:
                    b = tkinter.Label(label_desc, text=str(products[i][j])+"EUR", font=("Times New Roman", 12, "bold"), bg="black", fg="white", borderwidth=4)
                elif j>1 and i <len(products)-1:
                    b = tkinter.Label(label_desc, text=str(products[i][j])+"€", font=("Times New Roman", 11, "bold"), bg="#ECF5FF", fg="#272727", borderwidth=2)
                elif j<=1:
                    b = tkinter.Label(label_desc, text=products[i][j], font=("Times New Roman", 11, "bold"), bg="#ECF5FF", fg="#272727", borderwidth=2)
                else:
                    b = tkinter.Label(label_desc, text=products[i][j], font=("Times New Roman", 11, "bold"), bg="#ECF5FF",borderwidth=2)

                b.grid(row=i, column=j)
                #print(products)


