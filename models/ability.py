class Habilidade:

    ############## Iniciando ##############
    def __init__(self,
        nome,
        descricao,
        efeito_oculto=False
    ):
        self._nome = nome
        self._descricao = descricao
        self._efeito_oculto = efeito_oculto

    @property
    def nome(self):
        return self._nome

    @property
    def descricao(self):
        return self._descricao

    @property
    def efeito_oculto(self):
        return self._efeito_oculto