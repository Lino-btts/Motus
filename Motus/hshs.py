import tkinter as tk

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Grille Tkinter")

# Dimensions de la grille
rows, cols = 10, 10

# Ajouter des widgets à la grille
for i in range(rows):
    for j in range(cols):
        cell = tk.Label(fenetre, text=f"{i},{j}", borderwidth=1, relief="solid", width=5, height=2)
        cell.grid(row=i, column=j)

# Lancer l'application
fenetre.mainloop()