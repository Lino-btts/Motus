# codé en utf 8
# Date 29/11/2025
# Auteur : Lino Battesti
# Le programme permet de créer la fenêtre 

from tkinter import Tk,Label, Entry, StringVar, Button
from game import mot




Window_width = 500
Window_height = 800


class Fenetre():
    def __init__(self,root,word):
        self.__window = root
        self.__width = Window_width
        self.__height = Window_height
        self.__word = word[0]
        self.__rows = 6
        self.__columns = len(self.__word)
        self.__a = 0
    def jeu(self):
        f = Label()
        self.__l = []
        l =[]
        for i in range(self.__rows):
            for j in range(self.__columns):
                cell = Label(self.__window, text= "" , borderwidth=1, relief="solid", width=5, height=2)
                cell.grid(row=i, column=j)
                l.append(cell)
            self.__l.append(l)
        self.__v = StringVar()
        tentative = Entry(self.__window, textvariable= self.__v)
        tentative.grid(row = 0, column = 15, padx=10)
        bouton = Button(self.__window, text = "Valider", command = self.k, width= 10 )
        bouton.grid(row = 1, column = 15, padx=10)
        return self.__window
    def k(self):
        mot = self.__v.get()
        for i in range(len(mot)) :
            if mot[i] == self.__word[i] :
                case = self.__l[self.__a][i]
                case.config(bg = "green", text = mot[i])
            if mot[i] != self.__word[i] :
                if mot[i] in self.__word :
                    case = self.__l[self.__a][i]
                    case.config(bg = "orange", text = mot[i])
                if mot[i] not in self.__word :
                    case = self.__l[self.__a][i]
                    case.config(bg = "red", text = mot[i])
        self.__a += 1
        if self.__a == 7 :
            msg = Label(self.__window, text = "Game Over !")
            msg.grid(row = 6, column = 15)
        if mot == self.__word :
            msg = Label(self.__window, text = "Bravo vous avez gagnez !")
            msg.grid(row = 6, column = 15)
        return self.__window
    
    
            





root = Tk()
root.geometry("500x300" )
f = Fenetre(root,mot)
f.jeu()
root.mainloop()


 