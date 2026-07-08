class Status:

    def __init__(self,
        hp,
        ataque,
        defesa,
        ataque_especial,
        defesa_especial,
        velocidade
    ):
        self._hp = hp
        self._ataque = ataque
        self._defesa = defesa
        self._ataque_especial = ataque_especial
        self._defesa_especial = defesa_especial
        self._velocidade = velocidade

    @property
    def hp(self):
        return self._hp

    @property
    def ataque(self):
        return self._ataque

    @property
    def defesa(self):
        return self._defesa

    @property
    def ataque_especial(self):
        return self._ataque_especial
    
    @property
    def defesa_especial(self):
        return self._defesa_especial
    
    @property
    def velocidade(self):
        return self._velocidade
    
    @property
    def total(self):
        return (self._hp
            + self._ataque
            + self._defesa
            + self._ataque_especial
            + self._defesa_especial
            + self._velocidade
        )