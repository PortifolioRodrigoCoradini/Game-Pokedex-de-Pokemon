from tkinter import *
from tkinter import ttk

############## Variáveis Globais ##############
CO1 = "#feffff" #Branco
COR_FUNDO = "#0b2337" #AzulEscuro

############## Criando Janela ##############
def criar_janela(titulo, largura, altura):
    janela = Tk()
    janela.title(titulo)
    janela.geometry(f"{largura}x{altura}")
    janela.configure(bg=COR_FUNDO)

    ttk.Separator(janela, orient=HORIZONTAL).pack(fill="x")

    style = ttk.Style(janela)
    style.theme_use("clam")
    return janela