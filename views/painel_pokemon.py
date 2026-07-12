from tkinter import Frame
from tkinter import Label
from utils.carregar_imagens import carregar_imagem

############## Iniciando ##############
class Painel_Pokemon(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(
            bg="#0b1e2d",
            relief="ridge",
            bd=2
        )

        self.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.criar_componentes()

    ############## Criar Labels Info Pokemons ##############
    def criar_componentes(self):
        self.label_imagem = Label(
            self,
            bg="white"
        )
        self.label_imagem.pack(pady=20)

        self.label_nome = Label(
            self,
            text="Nome",
            font=("Segoe UI", 22, "bold"),
            bg="white"
        )
        self.label_nome.pack()

        self.label_id = Label(
            self,
            text="#000",
            font=("Segoe UI", 15),
            bg="white"
        )
        self.label_id.pack()

        self.label_tipo = Label(
            self,
            text="Tipo",
            font=("Segoe UI", 14),
            bg="white"
        )
        self.label_tipo.pack()

        # Componentes de Status
        self.label_hp = Label(self, text="HP: -", font=("Segoe UI", 11), bg="white")
        self.label_hp.pack()
        
        self.label_ataque = Label(self, text="Ataque: -", font=("Segoe UI", 11), bg="white")
        self.label_ataque.pack()

        self.label_defesa = Label(self, text="Defesa: -", font=("Segoe UI", 11), bg="white")
        self.label_defesa.pack()

        self.label_velocidade = Label(self, text="Velocidade: -", font=("Segoe UI", 11), bg="white")
        self.label_velocidade.pack()

        self.label_total = Label(self, text="Total: -", font=("Segoe UI", 12, "bold"), bg="white")
        self.label_total.pack(pady=5)

        # Componentes de Habilidades
        self.label_habilidades_titulo = Label(self, text="Habilidades:", font=("Segoe UI", 12, "underline"), bg="white")
        self.label_habilidades_titulo.pack(pady=(10, 0))

        self.label_habilidade1 = Label(self, text="-", font=("Segoe UI", 11), bg="white")
        self.label_habilidade1.pack()

        self.label_habilidade2 = Label(self, text="-", font=("Segoe UI", 11), bg="white")
        self.label_habilidade2.pack()

    ############## Método para Atualizar com Objeto Pokemon ##############
    def atualizar_dados(self, pokemon):
        """
        Recebe um objeto completo da classe Pokemon (Models) 
        e renderiza dinamicamente na tela.
        """
        # 1. Pega a cor do primeiro tipo do Pokémon para mudar o fundo do painel
        cor_fundo = pokemon.tipos[0].cor if pokemon.tipos else "#ffffff"
        
        # Atualiza a cor de fundo do Frame e de todas as Labels
        self.configure(bg=cor_fundo)
        for widget in self.winfo_children():
            widget.configure(bg=cor_fundo)
            
        # 2. Dados básicos
        self.label_nome.configure(text=pokemon.nome.capitalize())
        self.label_id.configure(text=f"#{pokemon.id:03d}")
        
        # Monta a string de tipos (Ex: "Grama / Veneno")
        nomes_tipos = [tipo.nome.capitalize() for tipo in pokemon.tipos]
        self.label_tipo.configure(text=" / ".join(nomes_tipos))
        
        # 3. Imagem do Pokémon
        try:
            # pokemon.imagem.oficial acessa a classe Imagens que você criou
            img_tk = carregar_imagem(pokemon.imagem.oficial, (238, 238))
            self.label_imagem.configure(image=img_tk)
            self.label_imagem.image = img_tk  # Mantém a referência na memória do Tkinter
        except Exception as e:
            print(f"Erro ao carregar a imagem do Pokémon: {e}")
            self.label_imagem.configure(image="")

        # 4. Status técnicos usando as properties da sua classe Status
        status_obj = pokemon.status
        self.label_hp.configure(text=f"HP: {status_obj.hp}")
        self.label_ataque.configure(text=f"Ataque: {status_obj.ataque}")
        self.label_defesa.configure(text=f"Defesa: {status_obj.defesa}")
        self.label_velocidade.configure(text=f"Velocidade: {status_obj.velocidade}")
        self.label_total.configure(text=f"Total: {status_obj.total}")

        # 5. Habilidades dinâmicas mapeando a sua classe Habilidade
        habilidades = pokemon.habilidades
        self.label_habilidade1.configure(text=habilidades[0].nome.capitalize() if len(habilidades) >= 1 else "-")
        self.label_habilidade2.configure(text=habilidades[1].nome.capitalize() if len(habilidades) >= 2 else "-")