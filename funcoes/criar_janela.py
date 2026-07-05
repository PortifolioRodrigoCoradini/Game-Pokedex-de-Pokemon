from tkinter import *
from tkinter import ttk

co1 = "#feffff" #Branco

############## Criando Janela ##############
def criar_janela(titulo, largura, altura):
    janela = Tk()
    janela.title(titulo)
    janela.geometry(f"{largura}x{altura}")
    janela.configure(bg=co1)

    ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

    style = ttk.Style(janela)
    style.theme_use("clam")
    return janela