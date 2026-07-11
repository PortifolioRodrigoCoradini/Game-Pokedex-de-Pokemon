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
                geracao,
                descricao,
                altura,
                peso,
                status,
                habitat,
                e_lendario,
                e_mitico,
                regiao,
                evolucoes,
                imagem
                ): 
        self._nome = nome
        self._id = id
        self._tipos = tipos
        self._habilidades = habilidades
        self._movimentos = movimentos
        self._geracao = geracao
        self._descricao = descricao
        self._altura = altura
        self._peso = peso
        self._status = status
        self._habitat = habitat
        self._e_lendario = e_lendario
        self._e_mitico = e_mitico
        self._regiao = regiao
        self._evolucoes = evolucoes
        self._imagem = imagem
        
    @property
    def nome(self):
        return self._nome
        
    @property
    def id(self):
        return self._id
        
    @property
    def tipos(self):
        return self._tipos
        
    @property
    def habilidades(self):
        return self._habilidades
        
    @property
    def movimentos(self):
        return self._movimentos
        
    @property
    def geracao(self):
        return self._geracao
        
    @property
    def descricao(self):
        return self._descricao
        
    @property
    def altura(self):
        return self._altura
        
    @property
    def peso(self):
        return self._peso
        
    @property
    def status(self):
        return self._status
        
    @property
    def habitat(self):
        return self._habitat
    
    @property
    def e_lendario(self):
        return "É lendário" if self._e_lendario else "Não é Lendário"

    @property
    def e_mitico(self):
        return "É Mítico" if self._e_mitico else "Não é mítico"
    
    @property
    def regiao(self):
        return self._regiao
    
    @property
    def evolucoes(self):
        return self._evolucoes
    
    @property
    def imagem(self):
        return self._imagem