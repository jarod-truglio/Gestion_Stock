import tkinter as tk
import tkinter.messagebox as messagebox
import mysql.connector

cnx = mysql.connector.connect(user='root', password='6666',
                              host='localhost',
                              database='boutique')
cursor = cnx.cursor()

def ajouter_produit():
    fenetre_saisie = tk.Toplevel(root)
    fenetre_saisie.title("Ajouter un produit")

    nom_label = tk.Label(fenetre_saisie, text="Nom")
    nom_label.grid(row=0, column=0)
    nom_entry = tk.Entry(fenetre_saisie)
    nom_entry.grid(row=0, column=1)

    description_label = tk.Label(fenetre_saisie, text="Description")
    description_label.grid(row=1, column=0)
    description_entry = tk.Entry(fenetre_saisie)
    description_entry.grid(row=1, column=1)

    prix_label = tk.Label(fenetre_saisie, text="Prix")
    prix_label.grid(row=2, column=0)
    prix_entry = tk.Entry(fenetre_saisie)
    prix_entry.grid(row=2, column=1)

    quantite_label = tk.Label(fenetre_saisie, text="Quantité")
    quantite_label.grid(row=3, column=0)
    quantite_entry = tk.Entry(fenetre_saisie)
    quantite_entry.grid(row=3, column=1)

    categorie_label = tk.Label(fenetre_saisie, text="Catégorie")
    categorie_label.grid(row=4, column=0)
    categorie_entry = tk.Entry(fenetre_saisie)
    categorie_entry.grid(row=4, column=1)

def modifier_produit(produit):
    fenetre_saisie = tk.Toplevel(root)
    fenetre_saisie.title("Modifier le produit")

    nom_label = tk.Label(fenetre_saisie, text="Nom")
    nom_label.grid(row=0, column=0)
    nom_entry = tk.Entry(fenetre_saisie)
    nom_entry.grid(row=0, column=1)
    nom_entry.insert(0, produit[1])

    description_label = tk.Label(fenetre_saisie, text="Description")
    description_label.grid(row=1, column=0)
    description_entry = tk.Entry(fenetre_saisie)
    description_entry.grid(row=1, column=1)
    description_entry.insert(0, produit[2])

    prix_label = tk.Label(fenetre_saisie, text="Prix")
    prix_label.grid(row=2, column=0)
    prix_entry = tk.Entry(fenetre_saisie)
    prix_entry.grid(row=2, column=1)
    prix_entry.insert(0, produit[3])

    quantite_label = tk.Label(fenetre_saisie, text="Quantité")
    quantite_label.grid(row=3, column=0)
    quantite_entry = tk.Entry(fenetre_saisie)
    quantite_entry.grid(row=3, column=1)
    quantite_entry.insert(0, produit[4])

    categorie_label = tk.Label(fenetre_saisie, text="Catégorie")
    categorie_label.grid(row=4, column=0)
    categorie_entry = tk.Entry(fenetre_saisie)
    categorie_entry.grid(row=4, column=1)
    categorie_entry.insert(0, produit[5])

    def valider():
        nom = nom_entry.get()
        description = description_entry.get()
        prix = float(prix_entry.get())
        quantite = int(quantite_entry.get())
        categorie = categorie_entry.get()

        query = ("INSERT INTO produit "
                 "(nom, description, prix, quantite, categorie) "
                 "VALUES (%s, %s, %s, %s, %s)")
        values = (nom, description, prix, quantite, categorie)
        cursor.execute(query, values)
        cnx.commit()

        fenetre_saisie.destroy()
        messagebox.showinfo("Produit ajouté", "Le produit a été ajouté à la base de données.")

    def valider_modif():
        nom = nom_entry.get()
        description = description_entry.get()
        prix = float(prix_entry.get())
        quantite = int(quantite_entry.get())
        categorie = categorie_entry.get()

        query = ("UPDATE produit "
                 "SET nom = %s, description = %s, prix = %s, quantite = %s, categorie = %s "
                 "WHERE id = %s")
        values = (nom, description, prix, quantite, categorie, produit[0])
        cursor.execute(query, values)
        cnx.commit()

        fenetre_saisie.destroy()
        messagebox.showinfo("Produit modifié", "Le produit a été modifié dans la base de données.")

    valider_button = tk.Button(fenetre_saisie, text="Valider", command=valider)
    valider_button.grid(row=5, column=0, columnspan=2)

    valider_button = tk.Button(fenetre_saisie, text="Valider", command=valider_modif)
    valider_button.grid(row=5, column=0, columnspan=2)

query = "SELECT * FROM produit"
cursor.execute(query)
produits = cursor.fetchall()

root = tk.Tk()
root.title("Gestion des produits")

text_box = tk.Text(root, height=10, width=50)
text_box.pack()

for produit in produits:
    text_box.insert(tk.END, f"{produit[1]} - {produit[2]} - {produit[3]} - {produit[4]}\n")

ajouter_button = tk.Button(root, text="Ajouter un produit", command=ajouter_produit)
ajouter_button.pack()

cursor.close()
cnx.close()

root.mainloop()