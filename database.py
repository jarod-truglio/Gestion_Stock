import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('boutique.db')
        self.cur = self.conn.cursor()

    def ajouter_produit(self, produit):
        self.cur.execute("INSERT INTO produits VALUES (NULL, ?, ?, ?, ?, ?)", produit)
        self.conn.commit()

    def supprimer_produit(self, id):
        self.cur.execute("DELETE FROM produits WHERE id=?", (id,))
        self.conn.commit()

    def modifier_produit(self, produit):
        self.cur.execute("UPDATE produits SET nom=?, description=?, prix=?, quantite=?, categorie=? WHERE id=?", produit)
        self.conn.commit()

    def afficher_produits(self):
        self.cur.execute("SELECT * FROM produits")
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()