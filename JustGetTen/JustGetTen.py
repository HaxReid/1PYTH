from tkinter import *
from tkinter import messagebox
from random import random
import time


class justGetTen:
    
    def __init__(self,taille):
        self.__row = taille
        self.__column = taille
        self.__tailleCarre = 80
        self.__grid= self.newBoard(self.__row)
        self.__maximum=self.__grid[0][0]
        self.__score=0
        self.__victoire=0
        self.__defaite=False

        self.__root=Tk()
        self.__root.configure(bg='papaya whip')
        self.__root.title("Just Get Ten")


        """""""""""""""FRAME CANVAS"""""""""""""""

        self.__frame1= Frame(self.__root)
        self.__frame1.grid(row=1,column=1,rowspan=3)
        self.__canvas=Canvas(self.__frame1)
        self.__canvas.config(height=self.__row*self.__tailleCarre, width=self.__column*self.__tailleCarre, highlightthickness=0, bd=0, bg="black")
        self.__canvas.bind("<Button-1>", self.justGetTen)
        self.__canvas.pack()
        

        """""""""""""""FRAME BOUTON"""""""""""""""

        self.__frame2=Frame(self.__root)
        self.__frame2.grid(row=1,column=0, padx=10)
        self.__frame2.configure(bg='papaya whip')


        """""""""""""""Bouton 4x4""""""""""""""" 

        self.__quatre = Button(self.__frame2, command = lambda: self.changeBoard(4, 160), text='4X4', padx=50, pady=27, bg='bisque', font=('Times New Roman', 16, 'bold'), fg="steel blue", borderwidth=0.5)
        self.__quatre.pack(pady=15, padx=(50, 0))


        """""""""""""""Bouton 5x5""""""""""""""" 

        self.__cinq = Button(self.__frame2, command = lambda: self.changeBoard(5, 128), text='5X5', padx=50, pady=27, bg='bisque', font=('Times New Roman', 16, 'bold'), fg="steel blue", borderwidth=0.5)
        self.__cinq.pack(pady=15, padx=(50, 0))


        """""""""""""""Bouton 6x6"""""""""""""""

        self.__six = Button(self.__frame2, command = lambda: self.changeBoard(6, 107), text='6X6', padx=50, pady=27, bg='bisque', font=('Times New Roman', 16, 'bold'), fg="steel blue", borderwidth=0.5)
        self.__six.pack(pady=15, padx=(50, 0))


        """""""""""""""Bouton 7x7"""""""""""""""

        self.__sept = Button(self.__frame2, command = lambda: self.changeBoard(7, 92), text='7X7', padx=50, pady=27, bg='bisque', font=('Times New Roman', 16, 'bold'), fg="steel blue", borderwidth=0.5)
        self.__sept.pack(pady=15, padx=(50, 0))


        """""""""""""""Bouton 8x8"""""""""""""""

        self.__huit = Button(self.__frame2, command = lambda: self.changeBoard(8, 80), text='8X8', padx=50, pady=27, bg='bisque', font=('Times New Roman', 16, 'bold'), fg="steel blue", borderwidth=0.5)
        self.__huit.pack(pady=15, padx=(50, 0))


        """""""""""""FRAME MEILLEUR"""""""""""""

        self.__frame3=Frame(self.__root)
        self.__frame3.grid(row=0, column=0)
        self.__frame3.configure(bg='papaya whip')
        self.__max = StringVar()
        self.__max.set("BEST - "+ str(self.maxi()))
        self.__text2= Label(self.__frame3, textvariable=self.__max, width=10, font=('Times New Roman', 20, 'bold'), fg="steel blue", bg="papaya whip")
        self.__text2.pack(pady=(10), padx=(50, 0))
        self.__total= StringVar()


        """""""""""""FRAME TOTAL"""""""""""""

        self.__frame5=Frame(self.__root)
        self.__frame5.grid(row=0, column=1)
        self.__frame5.configure(bg='papaya whip')
        self.__total.set(str(self.__score))
        self.__text1= Label(self.__frame5, textvariable=self.__total, width=30, font=('Courrier', 35, 'bold'), fg="steel blue", bg="papaya whip")
        self.__text1.pack(pady=(16, 35))


        """""""""""""FRAME MESSAGE"""""""""""""

        self.__frame4=Frame(self.__root)
        self.__frame4.grid(row=4, column=1)
        self.__frame4.configure(bg='papaya whip')
        self.__msg = StringVar()
        self.__msg.set("- TRY TO REACH TEN -")
        self.__text3= Label(self.__frame4, textvariable=self.__msg, width=30, font=('Times New Roman', 11, 'bold'), fg="steel blue", bg="papaya whip")
        self.__text3.pack(pady=(15, 25))
        
        self.display()
        self.__root.mainloop()





    """""""""""""""Fonction principale"""""""""""""""

    def justGetTen(self,event):
            clickRow = event.y//self.__tailleCarre
            clickColumn = event.x//self.__tailleCarre
            if self.possible(clickRow, clickColumn):
                currentState = self.__grid[clickRow][clickColumn]
                self.__grid[clickRow][clickColumn] += 1
                self.__score += self.__grid[clickRow][clickColumn]-1
                self.fusion(clickRow,clickColumn,currentState)
                self.__max.set("BEST - "+ str(self.maxi()))
                self.__total.set(str(self.__score))
                self.gravite()
                self.updateNumber()
                self.display()
                if self.__defaite == True:
                    messagebox.showinfo(title="Lose", message="You'll never getting Ten")
                if self.maxi() == 10 and self.__victoire == 0:
                    messagebox.showinfo(title="win", message="You Just Get Ten !")
                    self.__victoire = 1
                    self.win()



    """""""""""""""Création du tableau""""""""""""""" 

    def newBoard(self,number):
            grid=[[0 for j in range(number)]for i in range(number)]
            for i in range(number):
                for j in range(number):
                    proba = random()
                    if proba < 0.05:
                        grid[i][j] = 4
                    elif proba < 0.3:
                        grid[i][j] = 3
                    elif proba < 0.6:
                        grid[i][j] = 2
                    else:
                        grid[i][j] = 1
            return grid   


    def color(self,i,j):
        if self.__grid[i][j] == 0:
            return ["papaya whip", ""]
        elif self.__grid[i][j] == 1:
            return ["deep sky blue", "1"]
        elif self.__grid[i][j] == 2:
            return ["green yellow", "2"]
        elif self.__grid[i][j] == 3:
            return ["tomato2", "3"]
        elif self.__grid[i][j] == 4:
            return ["MediumPurple4", "4"]
        elif self.__grid[i][j] == 5:
            return ["SeaGreen1", "5"]
        elif self.__grid[i][j] == 6:
            return ["orchid1", "6"]
        elif self.__grid[i][j] == 7:
            return ["yellow4", "7"]
        elif self.__grid[i][j] == 8:
            return ["red", "8"] 
        elif self.__grid[i][j] == 9:
            return ["PaleGreen", "9"]
        elif self.__grid[i][j] == 10:
            return ["Gold", "10"]
        elif self.__grid[i][j] == 11:
            return ["Gold", "11"]
        elif self.__grid[i][j] == 12:
            return ["Gold", "12"]
        elif self.__grid[i][j] == 13:
            return ["Gold", "13"]
        elif self.__grid[i][j] == 14:
            return ["Gold", "14"]
        elif self.__grid[i][j] == 15:
            return ["Gold", "15"]


    def changeBoard(self, number, taille):
        self.__row, self.__column = number, number
        self.__tailleCarre = taille
        self.__grid = self.newBoard(number)
        self.__maximum=self.__grid[0][0]
        self.__score=0
        self.__max.set("BEST - "+ str(self.maxi()))
        self.__total.set(str(self.__score))
        self.__frame3.update()
        self.display()
        self.__victoire=0



    """""""""""""""Affichage"""""""""""""""

    def display(self):
        self.__canvas.delete(ALL)
        for i in range(self.__row):
            for j in range(self.__column):
                self.__canvas.create_rectangle(j*self.__tailleCarre,i*self.__tailleCarre,j*self.__tailleCarre+self.__tailleCarre,i*self.__tailleCarre+self.__tailleCarre, outline='white', width=2, fill=self.color(i,j)[0])
                self.__canvas.create_text((j*self.__tailleCarre) + self.__tailleCarre//2, (i*self.__tailleCarre) + self.__tailleCarre//2, text=self.color(i,j)[1], font=("Arial", 15, 'bold'))
        self.__canvas.update()



    """""""""""""""Règles du jeu""""""""""""""" 

    def possible(self,Xrow,Ycolumn):
            if Xrow>=1 and self.__grid[Xrow-1][Ycolumn] == self.__grid[Xrow][Ycolumn]:
                return True 
            if Xrow<self.__row-1 and self.__grid[Xrow+1][Ycolumn] == self.__grid[Xrow][Ycolumn]:
                return True   
            if Ycolumn>=1 and self.__grid[Xrow][Ycolumn-1] == self.__grid[Xrow][Ycolumn]:
                return True
            if Ycolumn<self.__column-1 and self.__grid[Xrow][Ycolumn+1] == self.__grid[Xrow][Ycolumn]:
                return True 
            else:
                return False
        

    def fusion(self,Xrow,Ycolumn,currentState):
        if Xrow>=1 and self.__grid[Xrow-1][Ycolumn] == currentState:
            self.__score += self.__grid[Xrow-1][Ycolumn]
            self.__grid[Xrow-1][Ycolumn] = 0
            self.fusion(Xrow-1,Ycolumn,currentState)
        if Xrow<self.__row-1 and self.__grid[Xrow+1][Ycolumn] == currentState:
            self.__score += self.__grid[Xrow+1][Ycolumn]
            self.__grid[Xrow+1][Ycolumn] = 0 
            self.fusion(Xrow+1,Ycolumn,currentState)
        if Ycolumn>=1 and self.__grid[Xrow][Ycolumn-1] == currentState:
            self.__score += self.__grid[Xrow][Ycolumn-1]
            self.__grid[Xrow][Ycolumn-1] = 0
            self.fusion(Xrow,Ycolumn-1,currentState)        
        if Ycolumn<self.__column-1 and self.__grid[Xrow][Ycolumn+1] == currentState:
            self.__score += self.__grid[Xrow][Ycolumn+1]
            self.__grid[Xrow][Ycolumn+1] = 0
            self.fusion(Xrow,Ycolumn+1,currentState)


    def gravite(self):
        continu = True
        while continu:
            continu = False
            for i in range(self.__row):
                for j in range(self.__column):
                    if i>=1 and self.__grid[i-1][j] > 0 and self.__grid[i][j] == 0:
                        self.__grid[i][j], self.__grid[i-1][j] = self.__grid[i-1][j], self.__grid[i][j]
                        self.display()
                        time.sleep(0.0001)
                        continu = True  
    

    def updateNumber(self):
        for i in range(self.__row):
            for j in range(self.__column):
                if self.__grid[j][i] == 0:
                    proba = random()
                    if proba < 0.05:
                        self.__grid[j][i] = 4
                        self.display()
                        time.sleep(0.0002)
                    elif proba < 0.3:
                        self.__grid[j][i] = 3
                        self.display()
                        time.sleep(0.0002)
                    elif proba < 0.6:
                        self.__grid[j][i] = 2
                        self.display()
                        time.sleep(0.0002)
                    else:
                        self.__grid[j][i] = 1
                        self.display()
                        time.sleep(0.0002)


    def win(self):
        if messagebox.askyesno(title="Ten !", message="Do you want to play again ?") == True:
            self.__canvas.delete("ALL")
            self.__score = 0
            self.__maximum=0
            self.__total.set(str(self.__score))
            self.__grid = self.newBoard(8)
            self.__max.set("BEST - "+ str(self.maxi()))
            self.display() 
            self.__victoire = 0


    def lose(self):
        for i in range(self.__row):
            for j in range(self.__column):
                if self.possible(i,j) == False:
                    self.__defaite == True
            



    """""""""""""""Fonction d'affichage en temps réel""""""""""""""" 

    def maxi(self):
        for i in range(self.__row):
            for j in range(self.__column):
                if self.__maximum < self.__grid[i][j]:
                    self.__maximum = self.__grid[i][j]
        return self.__maximum            


                    
justGetTen=justGetTen(8)