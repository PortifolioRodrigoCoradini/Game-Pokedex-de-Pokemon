from tkinter import Frame, Label
from utils.carregar_imagens import carregar_imagem

class Painel_Pokemon(Frame):
    def __init__(self, master):
        # Mudamos a cor padrão do frame base para combinar com o tema escuro
        super().__init__(master, bg="#0b1e2d", relief="ridge", bd=2)

        self.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )
        
        self.criar_componentes()

    def criar_componentes(self):
        # 🌌 ADICIONANDO A IMAGEM DE FUNDO TECNOLÓGICA
        # Criamos um label de fundo que cobrirá todo o painel
        self.label_fundo_tela = Label(self)
        self.label_fundo_tela.place(x=0, y=0, relwidth=1, relheight=1)
        
        try:
            # Carrega e redimensiona a imagem para caber na tela do painel
            self.img_fundo = carregar_imagem("images/fundo_tecnologico.png", (1200, 900))
            self.label_fundo_tela.configure(image=self.img_fundo)
        except Exception as e:
            print(f"Não foi possível carregar o fundo tecnológico: {e}")
            self.label_fundo_tela.configure(bg="#0b1e2d")

        # 🎨 CONFIGURAÇÃO DE CORES DO TEMA ESCURO
        cor_fundo_labels = "#102a43" # Um azul escuro tecnológico para os blocos de texto
        cor_texto_claro = "#e2e8f0"  # Branco acinzentado super legível
        cor_destaque = "#00f0ff"     # Azul ciano neon para ID e Títulos

        # Container para a foto do Pokemon (centralizado por cima do fundo)
        self.label_imagem = Label(self, bg=cor_fundo_labels, bd=2, relief="groove")
        self.label_imagem.pack(pady=(40, 10))

        # Informações Básicas
        self.label_nome = Label(self, text="Nome", font=("Segoe UI", 24, "bold"), bg=cor_fundo_labels, fg=cor_texto_claro)
        self.label_nome.pack(pady=2)

        self.label_id = Label(self, text="#000", font=("Segoe UI", 16, "bold"), bg=cor_fundo_labels, fg=cor_destaque)
        self.label_id.pack(pady=2)

        self.label_tipo = Label(self, text="Tipo", font=("Segoe UI", 14), bg=cor_fundo_labels, fg=cor_texto_claro)
        self.label_tipo.pack(pady=5)

        # Container invisível para organizar os Status e Habilidades lado a lado de forma moderna
        self.frame_status = Frame(self, bg=cor_fundo_labels, padx=15, pady=15, bd=1, relief="solid")
        self.frame_status.pack(pady=15)

        # Status Técnicos
        self.label_hp = Label(self.frame_status, text="HP: -", font=("Segoe UI", 12), bg=cor_fundo_labels, fg=cor_texto_claro)
        self.label_hp.pack(anchor="w")
        
        self.label_ataque = Label(self.frame_status, text="Ataque: -", font=("Segoe UI", 12), bg=cor_fundo_labels, fg=cor_texto_claro)
        self.label_ataque.pack(anchor="w")

        self.label_defesa = Label(self.frame_status, text="Defesa: -", font=("Segoe UI", 12), bg=cor_fundo_labels, fg=cor_texto_claro)
        self.label_defesa.pack(anchor="w")

        self.label_velocidade = Label(self.frame_status, text="Velocidade: -", font=("Segoe UI", 12), bg=cor_fundo_labels, fg=cor_texto_claro)
        self.label_velocidade.pack(anchor="w")

        self.label_total = Label(self.frame_status, text="Total: -", font=("Segoe UI", 13, "bold"), bg=cor_fundo_labels, fg=cor_destaque)
        self.label_total.pack(anchor="w", pady=(5, 0))

        # Habilidades
        self.label_habilidades_titulo = Label(self, text="HABILIDADES", font=("Segoe UI", 12, "bold"), bg=cor_fundo_labels, fg=cor_destaque)
        self.label_habilidades_titulo.pack(pady=(10, 2))

        self.label_habilidade1 = Label(self, text="-", font=("Segoe UI", 12), bg=cor_fundo_labels, fg=cor_texto_claro)
        self.label_habilidade1.pack()

        self.label_habilidade2 = Label(self, text="-", font=("Segoe UI", 12), bg=cor_fundo_labels, fg=cor_texto_claro)
        self.label_habilidade2.pack()

    def atualizar_dados(self, pokemon):
        """
        Recebe o objeto Pokemon e atualiza os textos sem destruir o tema escuro.
        """
        # Dados básicos
        self.label_nome.configure(text=pokemon.nome.upper())
        self.label_id.configure(text=f"#{pokemon.id:03d}")
        
        nomes_tipos = [tipo.nome.upper() for tipo in pokemon.tipos]
        self.label_tipo.configure(text=" | ".join(nomes_tipos))
        
        # Imagem do Pokémon
        try:
            img_tk = carregar_imagem(pokemon.imagem.oficial, (250, 250))
            self.label_imagem.configure(image=img_tk)
            self.label_imagem.image = img_tk
        except Exception as e:
            print(f"Erro ao carregar a imagem do Pokémon: {e}")

        # Status técnicos
        status_obj = pokemon.status
        self.label_hp.configure(text=f"HP: {status_obj.hp}")
        self.label_ataque.configure(text=f"ATK: {status_obj.ataque}")
        self.label_defesa.configure(text=f"DEF: {status_obj.defesa}")
        self.label_velocidade.configure(text=f"SPD: {status_obj.velocidade}")
        self.label_total.configure(text=f"TOTAL: {status_obj.total}")

        # Habilidades
        habilidades = pokemon.habilidades
        self.label_habilidade1.configure(text=habilidades[0].nome.upper() if len(habilidades) >= 1 else "-")
        self.label_habilidade2.configure(text=habilidades[1].nome.upper() if len(habilidades) >= 2 else "-")