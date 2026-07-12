class Evolucoes:

    ############## Iniciando ##############
    def __init__(self,
                nome,
                url,
                metodo=None,
                nivel=None,
                item=None
                ):
        self._nome = nome
        self._url = url
        self._metodo = metodo
        self._nivel = nivel
        self._item = item

    @property
    def nome(self):
        return self._nome
    
    @property
    def url(self):
        return self._url
    
    @property
    def metodo(self):
        return self._metodo
    
    @property
    def nivel(self):
        return self._nivel
    
    @property
    def item(self):
        return self._item