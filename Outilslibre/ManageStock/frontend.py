import tkinter# conda install -c anaconda tk
import controller 


def manage_checkout(window):
    #Erease window
    erease_window(window)
    window.title("Manage Chekout")
    screen_x = 1500
    screen_y = 820
    pos_x = int(window.winfo_screenwidth())//2 - screen_x//2
    pos_y = int(window.winfo_screenheight())//2 - screen_y//2
    win_size = "{}x{}+{}+{}".format(screen_x, screen_y, pos_x, pos_y)
    window.geometry(win_size)
    #
    head_desc = tkinter.Label(window, text="Stock Management", font=("helvetica", 25, "bold"),  fg="#003D79", borderwidth=2)
    head_desc.place(relx=0.42, rely=0.02)
    #Button
    button = tkinter.Button(window, text="Display articles", font=("Times New Roman", 15, "bold"), bg="#4160fd", fg='white',
                    activebackground="#2894FF", activeforeground="white", borderwidth=2, command=lambda:controller.get_all_products(window, entry_product_desc, label_rupture_desc, entry_rupture_desc)) # command=signup
    button.place(relx=0.07, rely=0.17)
    #Description
    label_product_desc = tkinter.Label(window, text="Products Description", font=("helvetica", 15, "bold"), fg="black", borderwidth=5)
    label_product_desc.place(relx=0.056, rely=0.12)
    entry_product_desc = tkinter.Label(window, font=("helvetica", 15, "bold"), width=50, heigh=20, bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_product_desc.place(relx=0.02, rely=0.25)

    
    #Description
    label_product_desc = tkinter.Label(window, text="Choose a receipt", font=("helvetica", 15, "bold"), fg="black", borderwidth=5)
    label_product_desc.place(relx=0.5, rely=0.12)
    #Button charge
    button = tkinter.Button(window, text="Charge Receipt", font=("Times New Roman", 12, "bold"), bg="#4160fd", fg='white',
                    activebackground="#2894FF", activeforeground="white", borderwidth=2, command=lambda:controller.charge_data_from_file(window, entry_receipt_desc)) # command=signup
    button.place(relx=0.45, rely=0.17)
    #Button validate
    button = tkinter.Button(window, text="Validate", font=("Times New Roman", 12, "bold"), bg="#01814A", fg='white',
                    activebackground="#01B468", activeforeground="white", borderwidth=2, command=lambda:controller.update_data_by_receipt(window, entry_product_desc, label_rupture_desc, entry_rupture_desc)) # command=signup
    button.place(relx=0.6, rely=0.17)
    entry_receipt_desc = tkinter.Label(window, font=("helvetica", 15, "bold"), width=40, heigh=10, bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_receipt_desc.place(relx=0.43, rely=0.25)

    #labels and entry 
    label_choose = tkinter.Label(window, text="Choose article to add or update", font=("helvetica", 15, "bold"),  fg="#003D79", borderwidth=5)
    label_choose.place(relx=0.75, rely=0.15)

    label_article_name = tkinter.Label(window, text="Product Name", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_article_name.place(relx=0.75, rely=0.2)
    entry_article_name = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_article_name.place(relx=0.85, rely=0.2)

    #Button Search article
    button_add =tkinter.Button(window, text="Search", font=("Times New Roman", 11, "bold"), bg="#4160fd", fg='white',
                    activebackground="#2894FF", activeforeground="white", borderwidth=2, command=lambda:controller.search_product(window, entry_article_name, entry_quantity,entry_price)) # command=signup
    button_add.place(relx=0.93, rely=0.25)

    label_quantity = tkinter.Label(window, text="Quantity    ", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_quantity.place(relx=0.75, rely=0.35)
    entry_quantity = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_quantity.place(relx=0.85, rely=0.35)

    label_price = tkinter.Label(window, text="Price       ", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_price.place(relx=0.75, rely=0.40)
    entry_price = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_price.place(relx=0.85, rely=0.40)
    #Button Update or add
    button_back = tkinter.Button(window, text="Add or Update", font=("Times New Roman", 15, "bold"), bg="#01814A", fg='white',
                    activebackground="#01B468", activeforeground="white", borderwidth=2, command=lambda:controller.add_or_update(window, entry_product_desc, entry_article_name, entry_quantity,entry_price, label_rupture_desc, entry_rupture_desc)) #  command=lambda:connexion(window)
    button_back.place(relx=0.83, rely=0.45)

    #Description de rupture de stock
    label_rupture_desc = tkinter.Label(window, font=("helvetica", 15, "bold"), fg="red", borderwidth=5)
    label_rupture_desc.place(relx=0.43, rely=0.55)
    entry_rupture_desc = tkinter.Label(window, font=("helvetica", 15, "bold"), width=50, heigh=10, borderwidth=2)
    entry_rupture_desc.place(relx=0.45, rely=0.6)
    

    
#This function try to erease all contents within the window
def erease_window(window):
    for widget in window.winfo_children():
        widget.destroy()


window = tkinter.Tk()
manage_checkout(window)

window.mainloop()

