from tkinter import Frame, Label
from utils.carregar_imagens import carregar_imagem

class Painel_Pokemon(Frame):
    def __init__(self, master):
        # Frame principal escuro
        super().__init__(master, bg="#0b1e2d", relief="flat")

        self.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )
        
        self.criar_componentes()

    def criar_componentes(self):
        # 🌌 Imagem de fundo tecnológica
        self.label_fundo_tela = Label(self, bg="#0b1e2d")
        self.label_fundo_tela.place(x=0, y=0, relwidth=1, relheight=1)
        
        try:
            self.img_fundo = carregar_imagem("images/fundo_tecnologico.png.jpg", (1200, 900))
            self.label_fundo_tela.configure(image=self.img_fundo)
        except Exception as e:
            print(f"Não foi possível carregar o fundo tecnológico: {e}")

        # 🖼️ CONTAINER DA IMAGEM DO POKÉMON (Com borda arredondada/estilizada)
        # Criamos um frame menor que servirá como uma "moldura" tecnológica para a foto
        self.moldura_imagem = Frame(
            self, 
            bg="#102230",          # Cor interna da moldura
            highlightbackground="#00f0ff", # Borda neon brilhante
            highlightthickness=3,  # Espessura da borda neon
            bd=0
        )
        # Ocupa um ótimo espaço vertical centralizado no topo
        self.moldura_imagem.pack(pady=(40, 20), padx=20)

        # Label da imagem principal (GIGANTE - 420x420 para cobrir quase tudo)
        self.label_imagem = Label(
            self.moldura_imagem,
            bg="#102230", # Fundo escuro uniforme por trás do Pokémon
            bd=0
        )
        self.label_imagem.pack(padx=15, pady=15) # Espaçamento interno para dar o efeito de borda/respiro

        # 🏷️ INFORMAÇÕES DO POKÉMON (Sem cor de fundo - integrado diretamente na tela)
        # Nome Grande e Bonito
        self.label_nome = Label(
            self,
            text="NOME",
            font=("Segoe UI", 32, "bold"),
            bg="#0b1e2d", # Mesma cor de fundo para "sumir" com a caixa da letra
            fg="#00f0ff"  # Cor Neon azul
        )
        self.label_nome.pack(pady=(10, 2))

        # ID do Pokémon
        self.label_id = Label(
            self,
            text="#000",
            font=("Segoe UI", 18, "bold"),
            bg="#0b1e2d",
            fg="#e2e8f0"  # Branco acinzentado suave
        )
        self.label_id.pack(pady=2)

        # Tipos do Pokémon
        self.label_tipo = Label(
            self,
            text="TIPO",
            font=("Segoe UI", 16, "italic"),
            bg="#0b1e2d",
            fg="#e2e8f0"
        )
        self.label_tipo.pack(pady=(2, 20))

        # ⚔️ CONTAINER DAS HABILIDADES (Mantido na parte inferior)
        self.frame_habilidades = Frame(self, bg="#102230", bd=2, relief="groove")
        self.frame_habilidades.pack(fill="x", padx=40, pady=(10, 30), side="bottom")

        self.label_habilidades_titulo = Label(
            self.frame_habilidades,
            text="HABILIDADES",
            font=("Segoe UI", 12, "bold"),
            bg="#102230",
            fg="#00f0ff"
        )
        self.label_habilidades_titulo.pack(pady=5)

        self.label_habilidade1 = Label(
            self.frame_habilidades,
            text="-",
            font=("Segoe UI", 11),
            bg="#102230",
            fg="#e2e8f0"
        )
        self.label_habilidade1.pack()

        self.label_habilidade2 = Label(
            self.frame_habilidades,
            text="-",
            font=("Segoe UI", 11),
            bg="#102230",
            fg="#e2e8f0"
        )
        self.label_habilidade2.pack(pady=(0, 10))

    def atualizar_dados(self, pokemon):
        """
        Recebe o objeto Pokémon e atualiza os elementos visuais.
        """
        nome_pokemon = pokemon.nome if hasattr(pokemon, 'nome') else pokemon._nome
        id_pokemon = pokemon.id if hasattr(pokemon, 'id') else pokemon._id
        
        # Atualiza os textos principais
        self.label_nome.configure(text=str(nome_pokemon).upper())
        self.label_id.configure(text=f"#{int(id_pokemon):03d}" if str(id_pokemon).isdigit() else f"#{id_pokemon}")
        
        # Tratamento seguro de Tipos
        lista_tipos = pokemon.tipos if hasattr(pokemon, 'tipos') else pokemon._tipos
        nomes_tipos = []
        for t in lista_tipos:
            if hasattr(t, 'nome'):
                nomes_tipos.append(t.nome.upper())
            elif isinstance(t, dict) and 'nome' in t:
                nomes_tipos.append(t['nome'].upper())
            else:
                nomes_tipos.append(str(t).upper())
                
        self.label_tipo.configure(text=" | ".join(nomes_tipos))
        
        # Faz o download/carrega a imagem oficial grande (400x400)
        try:
            img_obj = pokemon.imagem if hasattr(pokemon, 'imagem') else pokemon._imagem
            caminho_imagem = img_obj._oficial if hasattr(img_obj, '_oficial') else img_obj.oficial
            
            # Aqui definimos o tamanho gigante da imagem (400, 400)
            img_tk = carregar_imagem(caminho_imagem, (400, 400))
            self.label_imagem.configure(image=img_tk)
            self.label_imagem.image = img_tk
        except Exception as e:
            print(f"Erro ao carregar a imagem do Pokémon: {e}")

        # Habilidades
        habilidades = pokemon.habilidades if hasattr(pokemon, 'habilidades') else pokemon._habilidades
        hab1 = habilidades[0].nome.upper() if len(habilidades) >= 1 else "-"
        hab2 = habilidades[1].nome.upper() if len(habilidades) >= 2 else "-"
        self.label_habilidade1.configure(text=hab1)
        self.label_habilidade2.configure(text=hab2)