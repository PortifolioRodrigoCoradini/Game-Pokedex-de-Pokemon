import requests
from models.pokemons import Pokemon
from services.tradutor import Tradutor
from models.status import Status

############## Variáveis ##############
qtd_movimentos = 6
qtd_habilidades = 3
GERACOES = {
    "generation-i": "1ª Geração",
    "generation-ii": "2ª Geração",
    "generation-iii": "3ª Geração",
    "generation-iv": "4ª Geração",
    "generation-v": "5ª Geração",
    "generation-vi": "6ª Geração",
    "generation-vii": "7ª Geração",
    "generation-viii": "8ª Geração",
    "generation-ix": "9ª Geração",
}
'''STATUS = {
    "hp": "HP",
    "attack": "Ataque",
    "defense": "Defesa",
    "special-attack": "Ataque Especial",
    "special-defense": "Defesa Especial",
    "speed": "Velocidade"
}'''

############## PokeAPI Classe ##############
class PokeAPI:
    ############## URLs ##############
    URL = "https://pokeapi.co/api/v2/pokemon/"

    ############## Método Buscar ##############
    def buscar(self, nome_pokemon):
        resposta = requests.get(self.URL + nome_pokemon.lower())
        resposta = resposta.json()
        especie = self._buscar_especies(resposta)

        ############## Transformar JSON em Objeto ##############
        info_poke = Pokemon(resposta["name"], 
                            resposta["id"], 
                            self._buscar_tipos(resposta),
                            self._buscar_movimentos(resposta),
                            self._buscar_habilidades(resposta),
                            self._buscar_descricao(resposta),
                            (f"{resposta["height"]/10:.1f}m"),
                            (f"{resposta["weight"]/10:.1f}kg"),
                            GERACOES[especie["generation"]["name"]],
                            self._buscar_status(resposta)
                            #imagem
                            #cor fundo
                            #Habitat
                            #cadeiaevolucao
                            #élendario
                            #émitico
                            #regiao
                            #fraquesas resistencias
                            )
        return info_poke
    
    ############## Pegar todos os Tipos ##############
    def _buscar_tipos(self, resposta):
        return [tipo["type"]["name"]
                for tipo in resposta["types"]
            ]

    ############## Pegar todos os Movimentos ##############
    def _buscar_movimentos(self, resposta):
        return [movimento["move"]["name"]
                for movimento in resposta["moves"][:qtd_movimentos]
            ]

    ############## Pegar todos as Habilidades ##############
    def _buscar_habilidades(self, resposta):
        return [habilidade["ability"]["name"]
                for habilidade in resposta["abilities"][:qtd_habilidades]
            ]

    ############## Pegar a Descrição ##############
    def _buscar_descricao(self, resposta):
        descricoes = self._buscar_especies(resposta)

        for entrada in descricoes["flavor_text_entries"]:
            if entrada["language"]["name"] == "en":
                descricao = entrada["flavor_text"]
                break
        ############## Traduzir a Descrição
        descricao_pt = Tradutor.traduzir(descricao)
        return descricao_pt
    
    ############## Pegar URL Espécies ##############
    def _buscar_especies(self, resposta):
        especie = requests.get(resposta["species"]["url"])
        return especie.json()
    
    ############## Pegar Status ##############
    def _buscar_status(self, resposta):
        return Status(
        hp=resposta["stats"][0]["base_stat"],
        ataque=resposta["stats"][1]["base_stat"],
        defesa=resposta["stats"][2]["base_stat"],
        ataque_especial=resposta["stats"][3]["base_stat"],
        defesa_especial=resposta["stats"][4]["base_stat"],
        velocidade=resposta["stats"][5]["base_stat"]
        )