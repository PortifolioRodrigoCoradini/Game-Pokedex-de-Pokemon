############## Cores do Tipo Pokemon ##############
eletrico = "#FCC719"
grama = "#49D0B0"
fogo = "#ED8A8B"
agua = "#76BEFE"
escuridao = "#BA68C8"
dragao = "#C29791"

############## Pokemon Classe ##############
class Pokemon:
    def __init__(self, 
                nome, 
                id,
                tipos,
                habilidades,
                movimentos,
                #geracao,
                descricao,
                altura,
                peso
                #imagem
                ): 
        self.nome = nome
        self.id = id
        self.tipo1 = tipos
        self.habilidades = habilidades
        self.movimentos = movimentos
        self.descricao = descricao
        self.altura = altura
        self.peso = peso