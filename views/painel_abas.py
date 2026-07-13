from tkinter import Frame, Label, Text, END
from tkinter import ttk

class Painel_Abas(Frame):
    def __init__(self, master):
        # Cores tecnológicas combinando com a primeira imagem
        self.cor_fundo_escura = "#0b1a24"
        self.cor_fundo_abas = "#102230"
        self.cor_texto_claro = "#e2e8f0"
        self.cor_neon = "#00f0ff"

        super().__init__(master, bg=self.cor_fundo_escura)
        self.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Configuração do Estilo do ttk.Notebook para deixá-lo escuro
        self.estilo = ttk.Style()
        self.estilo.configure("Custom.TNotebook", background=self.cor_fundo_escura, borderwidth=0)
        self.estilo.configure("Custom.TNotebook.Tab", 
                              background=self.cor_fundo_abas, 
                              foreground=self.cor_fundo_escura, # Cor do texto da aba não selecionada
                              font=("Segoe UI", 11, "bold"), 
                              padding=[15, 5])
        self.estilo.map("Custom.TNotebook.Tab",
                        background=[("selected", self.cor_fundo_abas)],
                        foreground=[("selected", self.cor_neon)])
        
        # Estilo personalizado para as Barras de Status neon
        self.estilo.configure("Status.Horizontal.TProgressbar", 
                              troughcolor="#0b1e2d", 
                              bordercolor="#102230", 
                              background="#00f0ff", 
                              lightcolor="#00f0ff", 
                              darkcolor="#00f0ff")
        
        # Criando o Notebook (Controlador das abas)
        self.notebook = ttk.Notebook(self, style="Custom.TNotebook")
        self.notebook.pack(fill="both", expand=True)

        self.criar_abas()

    def criar_abas(self):
        # 1º: Criamos as estruturas (Frames) de TODAS as abas primeiro
        self.aba_status = Frame(self.notebook, bg=self.cor_fundo_abas)
        self.aba_movimentos = Frame(self.notebook, bg=self.cor_fundo_abas)
        self.aba_info = Frame(self.notebook, bg=self.cor_fundo_abas)

        # 2º: Adicionamos as abas criadas no notebook
        self.notebook.add(self.aba_status, text="STATUS")
        self.notebook.add(self.aba_movimentos, text="MOVIMENTOS")
        self.notebook.add(self.aba_info, text="INFO GERAL")

        # 3º: Agora que todas as abas existem, criamos os componentes delas com segurança!
        self.criar_componentes_status()
        self.criar_componentes_movimentos()
        self.criar_componentes_info()

    def criar_componentes_status(self):
        # Configuração das colunas (Coluna 0: Nome, Coluna 1: Número, Coluna 2: Barra)
        self.aba_status.grid_columnconfigure(0, weight=1)
        self.aba_status.grid_columnconfigure(1, weight=1)
        self.aba_status.grid_columnconfigure(2, weight=3)

        self.labels_status = {}
        self.barras_status = {}  # Novo dicionário para guardar as barras
        atributos = ["HP", "Ataque", "Defesa", "Ataque Especial", "Defesa Especial", "Velocidade", "Total"]
        
        for i, attr in enumerate(atributos):
            # Nome do atributo
            lbl_title = Label(
                self.aba_status, 
                text=attr.upper(), 
                font=("Segoe UI", 10, "bold"), 
                bg=self.cor_fundo_abas, 
                fg=self.cor_texto_claro
            )
            lbl_title.grid(row=i, column=0, sticky="w", padx=(20, 10), pady=8)

            # Valor numérico
            lbl_val = Label(
                self.aba_status, 
                text="-", 
                font=("Segoe UI", 10, "bold"), 
                bg=self.cor_fundo_abas, 
                fg=self.cor_texto_claro
            )
            lbl_val.grid(row=i, column=1, sticky="e", padx=(10, 20), pady=8)
            self.labels_status[attr] = lbl_val

            # Barra de progresso gráfica (Não criamos para o "Total")
            if attr != "Total":
                barra = ttk.Progressbar(
                    self.aba_status,
                    style="Status.Horizontal.TProgressbar",
                    orient="horizontal",
                    length=150,
                    mode="determinate",
                    maximum=255  # Limite máximo de status base em Pokémon
                )
                barra.grid(row=i, column=2, sticky="w", padx=(0, 20), pady=8)
                self.barras_status[attr] = barra

    def criar_componentes_movimentos(self):
        # Caixa de texto estilizada com scroll para listar todos os movimentos da PokeAPI
        lbl_titulo = Label(self.aba_movimentos, text="LISTA DE MOVIMENTOS DISPONÍVEIS:", 
                           font=("Segoe UI", 11, "bold"), bg=self.aba_movimentos.cget('bg'), fg=self.cor_neon)
        lbl_titulo.pack(anchor="w", padx=20, pady=10)

        self.txt_movimentos = Text(self.aba_movimentos, bg=self.cor_fundo_escura, fg=self.cor_texto_claro, 
                                   font=("Consolas", 11), insertbackground=self.cor_neon, bd=1, relief="solid")
        self.txt_movimentos.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    def criar_componentes_info(self):
        # Descrição da Pokédex
        lbl_desc_titulo = Label(self.aba_info, text="DESCRIÇÃO:", font=("Segoe UI", 11, "bold"), 
                               bg=self.aba_movimentos.cget('bg'), fg=self.cor_neon)
        lbl_desc_titulo.pack(anchor="w", padx=20, pady=(15, 5))

        self.lbl_descricao = Label(self.aba_info, text="-", font=("Segoe UI", 11), 
                                   bg=self.aba_movimentos.cget('bg'), fg=self.cor_texto_claro, justify="left", wraplength=450)
        self.lbl_descricao.pack(anchor="w", padx=20, pady=5)

        # Informações Extras de Altura, Peso e Região
        self.lbl_extras = Label(self.aba_info, text="Altura: -\nPeso: -\nRegião: -", 
                                font=("Segoe UI", 11), bg=self.aba_movimentos.cget('bg'), fg=self.cor_texto_claro, justify="left")
        self.lbl_extras.pack(anchor="w", padx=20, pady=20)

    def atualizar_abas_dados(self, pokemon):
        """
        Popula todas as abas dinamicamente convertendo os valores de texto da API de forma segura.
        """
        # 1. Atualizando Status (Numérico e Gráfico)
        status_obj = pokemon.status if hasattr(pokemon, 'status') else pokemon._status
        
        valores = {
            "HP": status_obj.hp,
            "Ataque": status_obj.ataque,
            "Defesa": status_obj.defesa,
            "Ataque Especial": status_obj.ataque_especial,
            "Defesa Especial": status_obj.defesa_especial,
            "Velocidade": status_obj.velocidade,
            "Total": status_obj.total
        }

        for attr, valor in valores.items():
            # Atualiza o texto do valor
            self.labels_status[attr].configure(text=str(valor))
            
            # Atualiza a barra de progresso correspondente
            if attr in self.barras_status:
                try:
                    num_valor = int(valor)
                    self.barras_status[attr]["value"] = num_valor
                except (ValueError, TypeError):
                    self.barras_status[attr]["value"] = 0

        # Aplica o destaque na linha do Total
        self.labels_status["Total"].configure(font=("Segoe UI", 11, "bold"), fg=self.cor_neon)

        # 2. Atualizando os Movimentos
        self.txt_movimentos.configure(state="normal")
        self.txt_movimentos.delete("1.0", END)
        lista_movimentos = pokemon.movimentos if hasattr(pokemon, 'movimentos') else []
        for move in lista_movimentos:
            self.txt_movimentos.insert(END, f"• {move.nome.upper().ljust(20)} | PP: {str(move.pp).ljust(3)} | Tipo: {move.tipo}\n")
        self.txt_movimentos.configure(state="disabled")

        # 3. Aba de Informações Gerais (Garante conversão segura de str para int)
        desc = pokemon.descricao if hasattr(pokemon, 'descricao') else pokemon._descricao
        self.lbl_descricao.configure(text=desc if desc else "Sem descrição disponível.")
        
        # Converte peso e altura limpando qualquer caractere não numérico se necessário
        try:
            alt_crua = pokemon.altura if hasattr(pokemon, 'altura') else pokemon._altura
            alt_num = float(''.join(filter(lambda x: x.isdigit() or x=='.', str(alt_crua))))
            altura_formatada = f"{alt_num / 10} m"
        except:
            altura_formatada = f"{pokemon._altura} m" if hasattr(pokemon, '_altura') else "- m"

        try:
            peso_cru = pokemon.peso if hasattr(pokemon, 'peso') else pokemon._peso
            peso_num = float(''.join(filter(lambda x: x.isdigit() or x=='.', str(peso_cru))))
            peso_formatado = f"{peso_num / 10} kg"
        except:
            peso_formatado = f"{pokemon._peso} kg" if hasattr(pokemon, '_peso') else "- kg"

        gen = pokemon.geracao if hasattr(pokemon, 'geracao') else pokemon._geracao
        hab = pokemon.habitat if hasattr(pokemon, 'habitat') else (pokemon._habitat if hasattr(pokemon, '_habitat') else 'Desconhecido')
        
        texto_extras = f"ALTURA: {altura_formatada}\nPESO: {peso_formatado}\nGERAÇÃO: {str(gen).upper()}\nHABITAT: {str(hab).upper()}"
        self.lbl_extras.configure(text=texto_extras)