from PIL import Image, ImageTk

def carregar_imagem(caminho, tamanho):
    imagem = Image.open(caminho)
    imagem = imagem.resize(tamanho)
    return ImageTk.PhotoImage(imagem)