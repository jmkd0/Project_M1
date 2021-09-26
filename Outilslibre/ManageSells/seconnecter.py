from random import random, randint
from tkinter import *
from tkinter.messagebox import showinfo, showerror, showwarning, askyesno
from os.path import *
from email.mime.text import MIMEText
from smtplib import *
from email.mime.multipart import *
from tkinter.filedialog import*



global nombre
nombre = randint(1, 100)
nombre2 = randint(100, 150)
nombre3 = randint(150, 200)
nombre4 = randint(200, 250)
nombre5 = randint(250, 300)
nombre6 = randint(300, 350)
nombre7 = randint(350, 400)
nombre8 = randint(400, 500)
nombre9 = randint(500, 700)


def niveau2(event):
    print(nombre2)
    print(nombre2)
    val = int(Entry8.get())
    coup = int(Entry9.get())
    c = coup + 1
    Entry9.config(state='normal')
    Entry9.delete("0", END)
    Entry9.insert(INSERT, c)
    Entry9.config(state='disable')
    if val < nombre2:
        text1.config(state="normal")
        text1.insert(INSERT, str(val) + "\n")
        text1.config(state="disable")
        text.config(state="normal")
        text.delete("1.0", END)
        text.insert(INSERT, "NIVEAU 2: Saisir une valeur entre 100 et 150\n", 'tag1')
        text.tag_config("tag1", foreground="#0037ff", font=("Times New Roman", 15, "bold"))
        text.insert(INSERT, "--->Trop petit!!")
        text.config(state="disable")
        Entry8.delete(0, END)
    elif val > nombre2:
        text1.config(state="normal")
        text1.insert(INSERT, str(val) + "\n")
        text1.config(state="disable")
        text.config(state="normal")
        text.delete('1.0', END)
        text.insert(INSERT, "NIVEAU 2: Saisir une valeur entre 100 et 150\n", "tag1")
        text.tag_config("tag1", foreground="#0037ff", font=("Times New Roman", 15, "bold"))
        text.insert(INSERT, "--->Trop grand!!")
        text.config(state="disable")
        Entry8.delete(0, END)
    else:
        text1.config(state="normal")
        text1.insert(INSERT, str(val) + "\n", 'win')
        text1.tag_config('win', foreground="#37ff00")
        text1.config(state="disable")
        text.config(state="normal")
        text.delete("1.0", END)
        text.insert(INSERT, "\n")
        text.insert(INSERT, "--->Felicitation!! gagné en {} coup(s)".format(c), 'fin')
        text.tag_config("fin", foreground="#37ff00", font=("Arial", 17, "bold"))
        text.config(state="disable")
        Entry8.delete(0, END)


def play(event):
    print(nombre)
    print(nombre)
    val = int(Entry8.get())
    coup = int(Entry9.get())
    c = coup + 1
    Entry9.config(state='normal')
    Entry9.delete("0", END)
    Entry9.insert(INSERT, c)
    Entry9.config(state='disable')
    if val < nombre:
        text1.config(state="normal")
        text1.insert(INSERT, str(val) + "\n")
        text1.config(state="disable")
        text.config(state="normal")
        text.delete("1.0", END)
        text.insert(INSERT, "NIVEAU 1: Saisir une valeur entre 1 et 100\n", 'tag1')
        text.tag_config("tag1", foreground="#0037ff", font=("Times New Roman", 15, "bold"))
        text.insert(INSERT, "--->Trop petit!!")
        text.config(state="disable")
        Entry8.delete(0, END)
    elif val > nombre:
        text1.config(state="normal")
        text1.insert(INSERT, str(val) + "\n")
        text1.config(state="disable")
        text.config(state="normal")
        text.delete('1.0', END)
        text.insert(INSERT, "NIVEAU 1: Saisir une valeur entre 1 et 100\n", "tag1")
        text.insert(INSERT, "--->Trop grand!!")
        text.config(state="disable")
        Entry8.delete(0, END)
        text1.config(state="normal")


    else:
        text1.insert(INSERT, str(val) + "\n", 'win')
        text1.tag_config('win', foreground="#37ff00")
        text.tag_config("tag1", foreground="#0037ff", font=("Times New Roman", 15, "bold"))
        text1.config(state="disable")
        text.config(state="normal")
        text.delete("1.0", END)
        text.insert(INSERT, "\n")
        text.insert(INSERT, "--->Felicitation!! gagné en {} coup(s)\nNiveau2: Saisir entre 100 et 150".format(c), 'fin')
        text.tag_config("fin", foreground="#37ff00", font=("Arial", 13, "bold"))
        text.config(state="disable")
        Entry8.delete(0, END)

        Entry10.config(state='normal')
        Entry10.delete("0", END)
        Entry10.insert(INSERT, 2)
        Entry10.config(state='disable')
        niveau2(event)






def mega_game():
    global win2
    win2 = Toplevel()
    windows.withdraw()
    color = "#717113"
    win2.title("GAME")
    win2.geometry("600x400")
    win2.resizable(width=0, height=0)
    win2.config(background=color)
    win2.iconbitmap("/home/komlan/anapro/python.ico")
    can3 = Canvas(win2, width=600, height=400, bg=color)
    photo3 = PhotoImage(file="/home/komlan/anapro/image1.jpg")
    can3.create_image(300, 200, anchor=CENTER, image=photo3)
    can3.pack()

    global Entry8
    global Entry9
    global Entry10
    global text
    global LabelFrame
    Entry8 = Entry(can3, font=("Times New Roman", 25, "bold"), width=20, bg="white", fg="black", highlightthickness="5",
                   highlightbackground='#2324AF', justify="center")
    Entry8.focus_set()
    Entry8.place(x=120, y=150)

    # Affichage du nombre de coups
    label8 = Label(can3, text="Coups ", font=("Times New Roman", 25, "bold", UNDERLINE), bg="#717113", fg="white")
    label8.place(x=12, y=150)
    Entry9 = Entry(can3, font=("Times New Roman", 25, "bold"), width=5, bg="#2A9BFF", fg="black",
                   highlightthickness="5",
                   highlightbackground='yellow', justify="center", borderwidth=3)
    Entry9.place(x=12, y=200)
    Entry9.insert(INSERT, "0")
    Entry9.config(state='disable')
    # Affichage du niveau
    label9 = Label(can3, text="Niveau", font=("Times New Roman", 25, "bold", UNDERLINE), bg="#717113", fg="white")
    label9.place(x=12, y=260)
    Entry10 = Entry(can3, font=("Times New Roman", 25, "bold"), width=5, bg="#2A9BFF", fg="black",
                    highlightthickness="5",
                    highlightbackground='yellow', justify="center", borderwidth=2)
    Entry10.place(x=12, y=310)
    Entry10.insert(INSERT, "1")
    Entry10.config(state='disable')

    # Affichage des resultats
    LabelFrame = LabelFrame(can3, text="MEGA GAME", font=("Times New Roman", 15, "bold"), fg="white", bg="#717113",
                            borderwidth=5, height=100, width=500, padx=5, pady=5)
    LabelFrame.place(x=50, y=30)
    text = Text(LabelFrame, font=("helvetica", 13, "bold"), height=3, width=53, fg="black")
    text.place(x=0, y=0)
    text.insert(INSERT, "LEVEL 1: Saisir entre 1 et 100", "n1")
    text.tag_config("n1", foreground="#111FAF", font=("Times New Roman", 20, "bold"), underline=True)
    text.config(state="disable")

    # Champ d'affichage des valeurs saisies
    global text1
    text1 = Text(can3, font=("helvetica", 13, "bold"), height=12, width=7, fg="black")
    text1.insert(INSERT, "INPUTS", "valeurs")
    text1.tag_config("valeurs", foreground="#161EAF", underline=True)
    text1.config(state="disable")
    text1.place(x=480, y=150)
    scrolbrar = Scrollbar(can3, command=text1.yview)
    scrolbrar.grid(padx=550, pady=150, ipady=30)
    text1.configure(yscrollcommand=scrolbrar.set)

    # Button de validation
    button = Button(can3, text="OK", font=("Times New Roman", 15, "bold"), bg="#4160fd", fg='white',
                    activebackground="#80ff00", activeforeground="#3caf22", padx=30, pady=0, command=play)
    win2.bind("<Return>", play or niveau2)

    button.place(x=220, y=220)
    # Creation d'un scroll bar

    win2.mainloop()


def valider(event):
    username = entry1.get()
    password = entry2.get()
    if not username or not password or " " in username or " " in password:
        entry1.delete(0, END)
        entry2.delete(0, END)
        showerror("Error", "username or password is incorrect")

    else:
        if isfile("users.txt"):
            with open("users.txt", 'r+') as fichier:
                for line in fichier:
                    a = line.strip('\n').split(";")
                    print(a)
                    if (a[0] == username) and (a[1] == password):
                        entry1.delete(0, END)
                        entry2.delete(0, END)
                        if askyesno("Congratulation!", "You will be redirected to a game continue?"):
                            mega_game()
                        else:
                            showinfo("Info", "TO SEE US VERY SOON!")

                    elif a[0] == username:
                        entry2.delete(0, END)
                        showinfo("Info", "wrong password click password forgot to check it")

                    else:
                        showwarning("error", "you have not registered please register to continue")
            fichier.close()
        else:
            entry1.delete(0, END)
            entry2.delete(0, END)
            showwarning("Error", "you have not registered please register to continue")


def confirmation(mail, username):
    sender_email = "ogmamarcellin@gmail.com"
    mail = "dankomaogma@gmail.com"
    subject = 'Mega Game'
    password = "Flava1996+"
    message = """
                {},WELCOME TO THE MEGA GAME AREA
                YOU HAVE BEEN WELL REGISTERED.
                MAKE YOURSELVES AT HOME.!!!
                    
                 Marcellin DANKOMA, Programmer.""".format(username)
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = mail
    msg["Subject"] = subject
    msg.attach(MIMEText(message))
    server = SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    texte = msg.as_string()
    server.sendmail(sender_email, mail, texte)
    server.quit()


def forg_password(mail, username, password):
    sender_email = "ogmamarcellin@gmail.com"
    subject = 'Mega Game'
    password1 = "Flava1996+"
    message = '''
                {},Your password is: " {} "
                 Marcellin DANKOMA, Programmer.'''.format(username, password)
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = mail
    msg["Subject"] = subject
    msg.attach(MIMEText(message))
    server = SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password1)
    texte = msg.as_string()
    server.sendmail(sender_email, mail, texte)
    server.quit()


def signup():
    mail = entry3.get()
    firstname = Entry4.get()
    username = Entry5.get()
    password = Entry6.get()
    cf_password = Entry7.get()
    if not password or not cf_password or " " in password or " " in cf_password or password != cf_password:
        showerror("Error", "Passwords do not match or are incorrect")
        Entry6.delete(0, END)
        Entry7.delete(0, END)
    elif not mail or not firstname or not username or " " in mail or ' ' in firstname or " " in username:
        showerror("Error", "Firstname / Username / Mail incorrect")
        entry3.delete(0, END)
        Entry4.delete(0, END)
        Entry5.delete(0, END)

    else:
        if isfile("userssign.txt"):
            fichier = open("users.txt", "r+")
            for line in fichier:
                a = line.strip('\n').split(";")
                print(a)
                if a[0] == username:
                    Entry5.delete(0, END)
                    showerror("Error", "username exists")

                else:

                    fichier = open("users.txt", "a+")
                    fichier.write(username + ';')
                    fichier.write(password + '\n')
                    entry1.delete(0, END)
                    entry2.delete(0, END)
                    showinfo("Welcome", "you have been successfully registered")
                    fichier2 = open("userssign.txt", "a+")
                    fichier2.write(mail + ';')
                    fichier2.write(firstname + ';')
                    fichier2.write(username + ';')
                    fichier2.write(password + ';')
                    fichier2.write(cf_password + '\n')
                    confirmation(mail, username)
                    fichier2.close()

            fichier.close()

        else:
            fichier = open("users.txt", "a+")
            fichier.write(username + ';')
            fichier.write(password + '\n')
            entry1.delete(0, END)
            entry2.delete(0, END)
            showinfo("Welcome", "you have been successfully signed")
            fichier.close()
            fichier2 = open("userssign.txt", "a+")
            fichier2.write(mail + ';')
            fichier2.write(firstname + ';')
            fichier2.write(username + ';')
            fichier2.write(password + ';')
            fichier2.write(cf_password + '\n')
            confirmation(mail, username)
            fichier2.close()


def register():
    win1 = Toplevel(windows)
    windows.withdraw()
    color = "#717113"
    win1.title("REGISTER")
    win1.geometry("600x400")
    win1.config(background=color)
    win1.iconbitmap("/home/komlan/anapro/python.ico")
    can2 = Canvas(win1, width=600, height=400, bg=color)
    photo2 = PhotoImage(file="/home/komlan/anapro/image2.jpg")
    can2.create_image(90, 50, anchor=NW, image=photo2)
    can2.pack()

    # Creation des labels
    label1 = Label(can2, text="Email: ", font=("Times New Roman", 15, "bold"), bg="#717113", fg="white")
    label1.place(x=10, y=60)
    label2 = Label(can2, text="Firstname: ", font=("Times New Roman", 15, "bold"), bg=color, fg="white")
    label2.place(x=10, y=110)
    label1 = Label(can2, text="Username: ", font=("Times New Roman", 15, "bold"), bg=color, fg="white")
    label1.place(x=10, y=170)
    label2 = Label(can2, text="Password: ", font=("Times New Roman", 15, "bold"), bg=color, fg="white")
    label2.place(x=10, y=230)
    label2 = Label(can2, text="Conf.Password: ", font=("Times New Roman", 15, "bold"), bg=color, fg="white")
    label2.place(x=10, y=280)

    # Entry creation
    global entry3
    global Entry4
    global Entry5
    global Entry6
    global Entry7
    entry3 = Entry(can2, font=("Times New Roman", 15, "bold"), width=30, bg="#aed0a4", fg="#e8063b", justify="center")
    entry3.focus_set()
    entry3.place(x=120, y=60)
    Entry4 = Entry(can2, font=("Times New Roman", 15, "bold"), bg="#aed0a4", fg="#e8063b", justify='center')
    Entry4.place(x=200, y=110)
    Entry5 = Entry(can2, font=("Times New Roman", 15, "bold"), bg="#aed0a4", fg="#e8063b", justify='center')
    Entry5.place(x=200, y=170)
    Entry6 = Entry(can2, font=("Times New Roman", 15, "bold"), show="*", bg="#aed0a4", fg="#e8063b", justify='center')
    Entry6.place(x=200, y=230)
    Entry7 = Entry(can2, font=("Times New Roman", 15, "bold"), show="*", bg="#aed0a4", fg="#e8063b", justify='center')
    Entry7.place(x=200, y=280)

    # Button de validation

    button = Button(can2, text="register", font=("Times New Roman", 15, "bold"), bg="#4160fd", fg='white',
                    activebackground="#80ff00", activeforeground="#3caf22", padx=30, pady=0, command=signup)
    button.place(x=140, y=330)

    win1.mainloop()


def chek_password():
    username = entry1.get()
    if not username or " " in username:
        entry1.delete(0, END)
        entry2.delete(0, END)
        showerror("Error", "username is invalid, Please re-enter")
    else:
        if isfile("userssign.txt"):
            with open("userssign.txt", 'r+') as fichier:
                for line in fichier:
                    a = line.strip('\n').split(";")
                    if a[2] == username:
                        mail = a[0]
                        password = a[3]
                        forg_password(mail, username, password)
                        showinfo("Congratulation!",
                                 "your password has been sent to your mailbox. Please consult it!. ".format(username))
                    else:
                        showwarning("error", "you have not registered please register to continue")
                        entry1.delete(0, END)
                        entry2.delete(0, END)
            fichier.close()
        else:
            showwarning("Error", "you have not registered please register to continue")
            entry1.delete(0, END)
            entry2.delete(0, END)


windows = Tk()
x = 600
y = 600
windows.geometry("{}x{}".format(x, y))
windows.config(bg="orange")

can = Canvas(windows, width=x, height=y, bg="#717113")
photo1 = PhotoImage(file="/home/komlan/anapro/image3.png")
can.create_image(275, 100, anchor=CENTER, image=photo1)
can.place(x=0, y=5)

# Creation des labels
label1 = Label(can, text="Username: ", font=("Times New Roman", 15, "bold"), bg="#717113", fg="white")
label1.place(x=45, y=40)
label2 = Label(can, text="Password: ", font=("Times New Roman", 15, "bold"), bg="#717113", fg="white")
label2.place(x=22, y=100)

# Creation des champs de saisie
entry1 = Entry(can, font=("Times New Roman", 15, "bold"), bg="#aed0a4", fg="#e8063b", justify="center")
entry1.focus_set()
entry1.place(x=145, y=40)
entry2 = Entry(can, font=("Times New Roman", 15, "bold"), show="*", bg="#aed0a4", fg="#e8063b")
entry2.place(x=145, y=100)

# Creation de button
button = Button(can, text="valid", font=("Times New Roman", 15, "bold"), bg="#717113", fg='white',
                activebackground="#80ff00", activeforeground="#2229af", padx=20, pady=0, command=valider)
windows.bind("<Return>", valider)
button.place(x=150, y=150)

button1 = Button(can, text="Password forgot", font=("Times New Roman", 15, "bold"), bg="#717113", fg='white',
                 activebackground="#80ff00", activeforeground="#2229af", padx=20, pady=0, command=chek_password)
button1.place(x=300, y=150)

# Deuxiemme partie du travail
# Ajustement du travail
# D'abord ajustons a nouveau notre travail

can1 = Canvas(windows, width=600, height=400, bg="#0ea598")
photo = PhotoImage(file="/home/komlan/anapro/image4.png")
can1.create_image(290, 200, anchor=CENTER, image=photo)
can1.place(x=0, y=195)

button2 = Button(can1, text="Sign in", font=("Times New Roman", 15, "bold"), bg="#4160fd", fg='white',
                 activebackground="#80ff00", activeforeground="#2229af", padx=20, pady=0, command=register)

button2.place(x=230, y=170)

windows.mainloop()
