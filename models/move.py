class Move:

    ############## iniciando ##############
    def __init__(self,
        nome,
        descricao,
        tipo,
        categoria,
        poder,
        precisao,
        pp
    ):
        self._nome = nome
        self._descricao = descricao
        self._tipo = tipo
        self._categoria = categoria
        self._poder = poder
        self._precisao = precisao
        self._pp = pp

    @property
    def nome(self):
        return self._nome

    @property
    def descricao(self):
        return self._descricao

    @property
    def tipo(self):
        return self._tipo

    @property
    def categoria(self):
        return self._categoria

    @property
    def poder(self):
        return self._poder

    @property
    def precisao(self):
        return self._precisao

    @property
    def pp(self):
        return self._pp