class Type:
    ############## Iniciando ##############
    def __init__(self,
        nome,
        cor,
        fraquezas,
        resistencias,
        imunidades
    ):
        self._nome = nome
        self._cor = cor
        self._fraquezas = fraquezas
        self._resistencias = resistencias
        self._imunidades = imunidades

    @property
    def nome(self):
        return self._nome
    
    @property
    def cor(self):
        return self._cor
    
    @property
    def fraquezas(self):
        return self._fraquezas
    
    @property
    def resistencias(self):
        return self._resistencias
    
    @property
    def imunidades(self):
        return self._imunidades