from tkinter import *
from PIL import Image

############## Cores ##############
co0 = "#403d3d" #Preto
co1 = "#feffff" #Branco

############## Carregar Labels ##############
### OBRIGATÓRIO:
#--JANELA
#--NUMERO_X
#--NUMERO_Y
def carregar_label(janela, numero_x, numero_y, texto="", fonte="Verdana 10", cor_back=co1, cor_letra=co0, estilo="flat", justificacao=CENTER):
    label = Label(janela, text=texto, font=fonte, bg=cor_back, fg=cor_letra, relief=estilo, anchor=justificacao)
    label.place(x=numero_x, y=numero_y)
    label.lift()
    return label