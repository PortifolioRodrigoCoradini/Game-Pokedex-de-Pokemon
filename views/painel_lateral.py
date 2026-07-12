from tkinter import Frame
from tkinter import Button
from utils.carregar_imagens import carregar_imagem
from tkinter import Entry
from tkinter import Canvas
from tkinter import Scrollbar

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
        self.botao_ativo = None

        self.configure(
            width=180,
            bg="#16344b",
            relief="ridge",
            bd=2
        )
        self.pack_propagate(False)
        self.pack(
            side="left",
            fill="y",
            padx=10,
            pady=10
        )
        self.criar_pesquisa()
        self.criar_lista()
        self.criar_botoes()

    ############## Iniciando Botões ##############
    def criar_botoes(self):
        self.imagens = []
        self.botoes = []

        ############## Criar Botão pros Pokemon ##############
        for i, (nome, dados) in enumerate(self.pokemons.items()):
            imagem = carregar_imagem(
                dados["Tipo"]["imagem_cabeca"],
                (45,45)
            )
            self.imagens.append(imagem)

            ############## Padrão Botão
            botao = Button(self.frame_lista,
                image=imagem,
                text=nome,
                compound="left",
                width=1,
                height=45,
                bg="#244d6b",
                fg="white",
                activebackground="#4d79ff",
                activeforeground="white",
                relief="flat",
                bd=0,
                cursor="hand2",
                anchor="w",
                padx=10
            )
            botao.config(
                command=lambda nome=nome, botao=botao:
                    self.selecionar_botao(botao, nome))

            botao.pack(fill="x", padx=5, pady=5)
            
            ############## Salvar Butões ##############
            self.botoes.append((nome.lower(), botao))

    ############## Colorir o Botão Selecionado ##############
    def selecionar_botao(self, botao, nome):
        # Se já existe um botão selecionado, volta a cor normal
        if self.botao_ativo:
            self.botao_ativo.config(bg="#244d6b")

        # Destaca o botão clicado
        botao.config(bg="#F7D02C")

        # Salva qual é o botão selecionado
        self.botao_ativo = botao

        # Chama a função da janela principal
        self.ao_clicar(nome)

    ############## Campo Pesquisa ##############
    def criar_pesquisa(self):
        self.pesquisa = Entry(
            self,
            font=("Segoe UI", 11)
        )

        self.pesquisa.pack(
            fill="x",
            padx=5,
            pady=10
        )

        self.pesquisa.bind(
            "<KeyRelease>",
            self.filtrar
        )

    ############## Criar Lista Lateral de Botões com Scroll ##############
    def criar_lista(self):
        self.canvas = Canvas(
            self,
            bg="#16344b",
            highlightthickness=0
        )

        self.scroll = Scrollbar(
            self,
            orient="vertical",
            command=self.canvas.yview
        )

        self.frame_lista = Frame(
            self.canvas,
            bg="#16344b"
        )

        self.frame_lista.bind(
            "<Configure>",
            lambda e:
            self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window(
            (0,0),
            window=self.frame_lista,
            anchor="nw"
        )

        self.id_frame = self.canvas.create_window(
            (0,0),
            window=self.frame_lista,
            anchor="nw"
        )
        
        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.itemconfig(
                self.id_frame,
                width=e.width
            ))

        self.canvas.configure(
            yscrollcommand=self.scroll.set
        )

        self.canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.scroll.pack(
            side="right",
            fill="y"
        )

    ############## Método Filtrar pokemon ##############
    def filtrar(self, event=None):
        texto = self.pesquisa.get().lower()

        for nome, botao in self.botoes:
            if texto in nome:
                botao.pack(
                    fill="x",
                    padx=5,
                    pady=3
                )
            else: 
                botao.pack_forget()