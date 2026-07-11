from tkinter import Frame
from tkinter import Button
from utils.carregar_imagens import carregar_imagem

class Painel_Lateral(Frame):
    ############## Iniciando ##############
    def __init__(self, 
                 master,
                pokemons,
                ao_clicar
            ):
        super().__init__(master)
        self.pokemons = pokemons
        self.ao_clicar = ao_clicar

        self.configure(
            width=220,
            bg="#16344b",
            relief="ridge",
            bd=2
        )
        self.pack(
            side="left",
            fill="y",
            padx=10,
            pady=10
        )
        self.criar_botoes()

    ############## Iniciando Botões ##############
    def criar_botoes(self):
        self.imagens = []

        for i, (nome, dados) in enumerate(self.pokemons.items()):
            imagem = carregar_imagem(
                dados["Tipo"]["imagem_cabeca"],
                (40,40)
            )

            self.imagens.append(imagem)

            botao = Button(self,
                image=imagem,
                text=nome,
                compound="left",
                width=180,
                command=lambda nome=nome:
                    self.ao_clicar(nome)
            )

            botao.pack(pady=4)