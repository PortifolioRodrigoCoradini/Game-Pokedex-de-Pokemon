import threading
from utils.criar_janela import criar_janela
from views.painel_lateral import Painel_Lateral
from views.painel_pokemon import Painel_Pokemon
from views.painel_abas import Painel_Abas
from services.pokeapi import PokeAPI
from dados import pokemons

LARGURA_JANELA = 1400
ALTURA_JANELA = 900

class Janela_Principal:
    def __init__(self):
        self.janela = criar_janela(
            "Pokedex Pokemon",
            LARGURA_JANELA,
            ALTURA_JANELA
        )
        self.janela.state("zoomed")
        
        # Dicionário de cache para guardar Pokémon já carregados e evitar requisições repetidas
        self.cache_pokemons = {}
        
        self.painel_lateral = Painel_Lateral(
            self.janela,
            pokemons,
            self.disparar_busca_pokemon  # Agora dispara o fluxo assíncrono
        )
        self.painel_pokemon = Painel_Pokemon(self.janela)
        self.painel_abas = Painel_Abas(self.janela)

    def disparar_busca_pokemon(self, nome):
        """
        Inicia uma nova Thread para buscar o Pokémon em segundo plano,
        evitando que a interface gráfica trave ou fique lenta.
        """
        # Feedback visual rápido de que algo está a carregar
        self.painel_pokemon.label_nome.configure(text="A CARREGAR...")
        
        # Se já buscámos este Pokémon antes, carrega instantaneamente do cache
        nome_busca = nome.lower()
        if nome_busca in self.cache_pokemons:
            pokemon_objeto = self.cache_pokemons[nome_busca]
            self.painel_pokemon.atualizar_dados(pokemon_objeto)
            self.painel_abas.atualizar_abas_dados(pokemon_objeto)
            return

        # Caso contrário, inicia a busca em segundo plano (Multithreading)
        tarefa = threading.Thread(target=self._tarefa_busca_background, args=(nome_busca,))
        tarefa.daemon = True  # Garante que a thread fecha se fechares o programa
        tarefa.start()

    def _tarefa_busca_background(self, nome):
        """Método que roda exclusivamente em segundo plano."""
        try:
            # 1. Busca os dados na API (demorado)
            api = PokeAPI()
            pokemon_objeto = api.buscar(nome)
            
            # 2. Salva no cache para acessos futuros instantâneos
            self.cache_pokemons[nome] = pokemon_objeto
            
            # 3. Atualiza os componentes visuais na thread principal de forma segura
            self.janela.after(0, self._atualizar_interface_sucesso, pokemon_objeto)
            
        except Exception as e:
            print(f"Erro ao buscar Pokémon na API: {e}")
            self.janela.after(0, self._atualizar_interface_erro)

    def _atualizar_interface_sucesso(self, pokemon_objeto):
        """Atualiza a UI de forma segura com os dados obtidos."""
        self.painel_pokemon.atualizar_dados(pokemon_objeto)
        self.painel_abas.atualizar_abas_dados(pokemon_objeto)

    def _atualizar_interface_erro(self):
        """Informa o utilizador em caso de falha de conexão."""
        self.painel_pokemon.label_nome.configure(text="ERRO DE CONEXÃO")