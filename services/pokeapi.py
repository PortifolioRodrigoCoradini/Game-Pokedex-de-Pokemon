import requests
from models.pokemons import Pokemon
from services.tradutor import Tradutor
from models.status import Status
from models.move import Move
from models.ability import Habilidade
from models.type import Type
from models.evolutions import Evolucoes
from models.imagens import Imagens

############## Variáveis Globais ##############
QTD_MOVIMENTOS = 8
QTD_HABILIDADES = 3
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
CORES_TIPO = {
    "normal": "#A8A77A",
    "fire": "#EE8130",
    "water": "#6390F0",
    "electric": "#F7D02C",
    "grass": "#7AC74C",
    "ice": "#96D9D6",
    "fighting": "#C22E28",
    "poison": "#A33EA1",
    "ground": "#E2BF65",
    "flying": "#A98FF3",
    "psychic": "#F95587",
    "bug": "#A6B91A",
    "rock": "#B6A136",
    "ghost": "#735797",
    "dragon": "#6F35FC",
    "dark": "#705746",
    "steel": "#B7B7CE",
    "fairy": "#D685AD",
}

REGIOES = {
    "generation-i": "Kanto",
    "generation-ii": "Johto",
    "generation-iii": "Hoenn",
    "generation-iv": "Sinnoh",
    "generation-v": "Unova",
    "generation-vi": "Kalos",
    "generation-vii": "Alola",
    "generation-viii": "Galar",
    "generation-ix": "Paldea"
}

############## PokeAPI Classe ##############
class PokeAPI:
    ############## URLs ##############
    URL = "https://pokeapi.co/api/v2/pokemon/"

    ############## Método Buscar ##############
    def buscar(self, nome_pokemon):
        resposta = requests.get(self.URL + nome_pokemon.lower())
        resposta = resposta.json()
        especie = self._pegar_url(resposta, "species")

        ############## Transformar JSON em Objeto ##############
        info_poke = Pokemon(resposta["name"], 
                            resposta["id"], 
                            self._buscar_tipos(resposta),
                            self._buscar_habilidades(resposta),
                            self._buscar_movimentos(resposta),
                            GERACOES[especie["generation"]["name"]],
                            self._buscar_descricao(especie["flavor_text_entries"], "flavor_text"),
                            (f"{resposta["height"]/10:.1f}m").replace(".", ","),
                            (f"{resposta["weight"]/10:.1f}kg").replace(".", ","),
                            self._buscar_status(resposta),
                            self._buscar_habitat(especie),
                            self._buscar_lendario(especie),
                            self._buscar_mitico(especie),
                            self._buscar_regiao(especie),
                            self._buscar_cadeia_evolutiva(especie),
                            self._buscar_imagem(resposta)
                            )
        return info_poke
    
    ############## Pegar todos os Tipos ##############
    def _buscar_tipos(self, resposta):
        tipos = []

        for tipo in resposta["types"]:
            info = self._pegar_url(tipo, "type")
            tipos.append(Type(
                    Tradutor.traduzir(info["name"]),
                    self._cor_tipo(info["name"]),
                    self._buscar_fraquezas(info),
                    self._buscar_resistencias(info),
                    self._buscar_imunidades(info)
                ))
        return tipos
    
    ############## Definindo as Cores ##############
    def _cor_tipo(self, nome):
        return CORES_TIPO.get(nome.lower(), "#777777")
    
    ############## Pegar Fraquezas ##############
    def _buscar_fraquezas(self, tipo):
        fraquezas = []

        for item in tipo["damage_relations"]["double_damage_from"]:
            fraquezas.append(
                Tradutor.traduzir(item["name"]))
        return fraquezas
    
    ############## Pegar Resistências ##############
    def _buscar_resistencias(self, tipo):
        resistencias = []

        for item in tipo["damage_relations"]["half_damage_from"]:
            resistencias.append(
                Tradutor.traduzir(item["name"]))
        return resistencias
    
    ############## Pegar Imunidades ##############
    def _buscar_imunidades(self, tipo):
        imunidades = []

        for item in tipo["damage_relations"]["no_damage_from"]:
            imunidades.append(
                Tradutor.traduzir(item["name"]))
        return imunidades

    ############## Pegar todos os Movimentos ##############
    def _buscar_movimentos(self, resposta):
        movimentos = []

        for movimento in resposta["moves"][:QTD_MOVIMENTOS]:
            move = self._pegar_url(movimento, "move")
            movimentos.append(Move(
                Tradutor.traduzir(move["name"]),
                self._buscar_descricao(move["effect_entries"], "effect"),
                Tradutor.traduzir(move["type"]["name"]),
                Tradutor.traduzir(move["damage_class"]["name"]),
                move["power"],
                move["accuracy"],
                move["pp"]
            ))
        return movimentos
    
    ############## Pegar todos as Habilidades ##############
    def _buscar_habilidades(self, resposta):
        habilidades = []

        for habil in resposta["abilities"][:QTD_HABILIDADES]:
            dados = self._pegar_url(habil, "ability")
            habilidades.append(Habilidade(
                Tradutor.traduzir(dados["name"]),
                self._buscar_descricao(dados["effect_entries"], "effect")
            ))
        return habilidades
    
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
    
    ############## Pegar Habitat ##############
    def _buscar_habitat(self, especie):
        habitat = especie["habitat"]
        if habitat is None:
            return "Desconhecido"
        return Tradutor.traduzir(habitat["name"])
    
    ############## É Lendário? ##############
    def _buscar_lendario(self, especie):
        return especie["is_legendary"]
    
    ############## É Mítico? ##############
    def _buscar_mitico(self, especie):
        return especie["is_mythical"]
    
    ############## Pegar Região ##############
    def _buscar_regiao(self, especie):
        return REGIOES[especie["generation"]["name"]]
    
    ############## Pegar Cadeia Evolução ##############
    def _buscar_cadeia_evolutiva(self, especie):
        cadeia_evolucao = self._pegar_url(especie, "evolution_chain")
        
        evolucoes = []
        self._percorrer_evolucao(cadeia_evolucao["chain"], evolucoes)
        return evolucoes
    
    ############## Percorrer Evoluções ##############
    def _percorrer_evolucao(self, etapa, evolucoes):
        nome = etapa["species"]["name"]
        metodo = None
        nivel = None
        item = None
        detalhes = etapa.get("evolution_details", [])

        if detalhes:
            detalhes = detalhes[0]
            if detalhes["trigger"]:
                metodo = detalhes["trigger"]["name"]
            nivel = detalhes["min_level"]
            if detalhes["item"]:
                item = detalhes["item"]["name"]

        evolucoes.append(Evolucoes(
                nome=Tradutor.traduzir(nome),
                url=etapa["species"]["url"],
                metodo=metodo,
                nivel=nivel,
                item=item
            ))

        for proxima_evolucao in etapa["evolves_to"]:
            self._percorrer_evolucao(proxima_evolucao, evolucoes)

    def _buscar_imagem(self, resposta):
            return Imagens(
                resposta["sprites"]["other"]["official-artwork"]["front_default"],
                resposta["sprites"]["other"]["official-artwork"]["front_shiny"]
            )
    
    #######-----------####### Utils #######-----------#######

    ############## Pegar URLs ##############
    def _pegar_url(self, json, palavra_chave="."):
        especie = requests.get(json[palavra_chave]["url"])
        return especie.json()
    
    ############## Pegar a Descrição  ##############
    @staticmethod
    def _buscar_descricao(json, palavra_chave, idioma="en"):
        for entrada in json:
            if entrada["language"]["name"] == idioma:
                return Tradutor.traduzir(entrada[palavra_chave])
        return "Sem descrição."