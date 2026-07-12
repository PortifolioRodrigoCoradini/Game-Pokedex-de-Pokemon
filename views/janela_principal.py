from utils.criar_janela import criar_janela
from views.painel_lateral import Painel_Lateral
from views.painel_pokemon import Painel_Pokemon
from services.pokeapi import PokeAPI
from dados import pokemons

############## Variáveis Globais ##############
LARGURA_JANELA = 1400
ALTURA_JANELA = 900

class Janela_Principal:
    ############## Iniciando ##############
    def __init__(self):
        self.janela = criar_janela(
            "Pokedex Pokemon",
            LARGURA_JANELA,
            ALTURA_JANELA
        )
        self.janela.state("zoomed")
        self.painel_lateral = Painel_Lateral(
            self.janela,
            pokemons,
            self.trocar_pokemon
        )
        self.painel_pokemon = Painel_Pokemon(self.janela)
        #self.criar_frames()
        #self.criar_menu()
        #self.criar_painel_lateral()
        #self.criar_painel_pokemon()
        #self.criar_abas()

    ############## Atualizar o Pokemon ##############
    def trocar_pokemon(self, nome):
        # 1. Instancia a PokeAPI
        api = PokeAPI()
        
        # 2. Busca os dados reais retornando o objeto da classe Pokemon
        pokemon_objeto = api.buscar(nome.lower())
        
        # 3. Envia o objeto diretamente para o Painel atualizar a tela
        self.painel_pokemon.atualizar_dados(pokemon_objeto)