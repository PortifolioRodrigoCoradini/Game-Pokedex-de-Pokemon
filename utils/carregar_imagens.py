from PIL import Image, ImageTk
import requests
from io import BytesIO

# Dicionário em memória para funcionar como Cache de Imagens já descarregadas/carregadas
CACHE_IMAGENS_MEMORIA = {}

def carregar_imagem(caminho, tamanho):
    # Gera uma chave única combinando o caminho e o tamanho desejado
    chave_cache = (caminho, tamanho)
    
    if chave_cache in CACHE_IMAGENS_MEMORIA:
        return CACHE_IMAGENS_MEMORIA[chave_cache]

    # Verifica se o caminho é uma URL da internet
    if str(caminho).startswith("http://") or str(caminho).startswith("https://"):
        try:
            resposta = requests.get(caminho, timeout=4)
            imagem = Image.open(BytesIO(resposta.content))
        except Exception as e:
            print(f"Erro ao descarregar imagem da URL ({caminho}): {e}")
            # Retorna uma imagem escura de fallback se falhar
            imagem = Image.new("RGB", tamanho, color="#0b1e2d")
    else:
        # Abre o ficheiro local do computador
        try:
            imagem = Image.open(caminho)
        except Exception as e:
            print(f"Erro ao carregar imagem local ({caminho}): {e}")
            imagem = Image.new("RGB", tamanho, color="#0b1e2d")
        
    imagem_redimensionada = imagem.resize(tamanho)
    imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)
    
    # Guarda no cache para a próxima vez ser instantâneo
    CACHE_IMAGENS_MEMORIA[chave_cache] = imagem_tk
    return imagem_tk