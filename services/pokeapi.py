import requests
from models.pokemons import Pokemon
from deep_translator import GoogleTranslator

############## Variáveis ##############
qtd_movimentos = 6
qtd_habilidades = 3

############## PokeAPI Classe ##############
class PokeAPI:
    ############## URLs ##############
    URL = "https://pokeapi.co/api/v2/pokemon/"

    ############## Método Buscar ##############
    def buscar(self, nome_pokemon):
        resposta = requests.get(self.URL + nome_pokemon.lower())
        resposta = resposta.json()

        ############## Pegar todos os Tipos ##############
        tipos = []
        for tipo in resposta["types"]:
            tipos.append(tipo["type"]["name"])

        ############## Pegar todos os Movimentos ##############
        movimentos = []
        for movimento in resposta["moves"][:qtd_movimentos]:
            movimentos.append(movimento["move"]["name"])

        ############## Pegar todos as Habilidades ##############
        habilidades = []
        for habilidade in resposta["abilities"][:qtd_habilidades]:
            habilidades.append(habilidade["ability"]["name"])

        ############## Pegar a Descrição ##############
        url_especie = resposta["species"]["url"]
        resposta_especies = requests.get(url_especie)
        descricoes = resposta_especies.json()

        for entrada in descricoes["flavor_text_entries"]:
            if entrada["language"]["name"] == "en":
                descricao = entrada["flavor_text"]
                break
        ############## Traduzir a Descrição
        descricao_pt = GoogleTranslator(source="en", target="pt").translate(descricao)


        ############## Transformar JSON em Objeto ##############
        info_poke = Pokemon(resposta["name"], 
                            resposta["id"], 
                            tipos,
                            movimentos,
                            habilidades,
                            descricao_pt,
                            (f"{resposta["height"]/10:.1f}m"),
                            (f"{resposta["weight"]/10:.1f}kg")
                            )
        return info_poke