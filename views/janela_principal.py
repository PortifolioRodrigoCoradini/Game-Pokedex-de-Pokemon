from utils.criar_janela import criar_janela
from views.painel_lateral import Painel_Lateral
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
        #self.criar_frames()
        #self.criar_menu()Pe
        #self.criar_painel_lateral()
        #self.criar_painel_pokemon()
        #self.criar_abas()

    def trocar_pokemon(self, nome):
        print(nome)