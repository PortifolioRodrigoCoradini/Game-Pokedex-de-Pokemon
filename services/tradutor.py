from deep_translator import GoogleTranslator

 ############## Traduzir a Descrição ##############
class Tradutor:
    def traduzir(texto, lingua="en"):
        return GoogleTranslator(
            source=lingua,
            target="pt").translate(texto)