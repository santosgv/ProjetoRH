from tkinter import *
from db import *
root=Tk()

class Aplicacao():

    def __init__(self):
        self.root=root
        self.Tela()
        self.frame()
        self.botoes()
        root.mainloop()
    def Tela(self):
        self.root.title('demissional')
        self.root.configure(background='black')
    def frame(self):
        self.main=Frame(self.root,bg='white')
        self.main.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)
    def botoes(self):
        self.lb=Label(self.main,text='consulta')
        self.lb.place(relx=0.1,rely=0.1)

Aplicacao()