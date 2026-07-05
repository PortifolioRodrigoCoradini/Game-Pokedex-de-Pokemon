from tkinter import *
from PIL import Image
from dados import pokemons
from funcoes.carregar_imagens import carregar_imagem
from funcoes.criar_janela import criar_janela
from funcoes.sorteio_pokemon import sorteio_pokemon

############## Cores ##############
co0 = "#444466" #Preto
co1 = "#feffff" #Branco
co2 = "#403d3d" #Preto_letra

############## Constantes ##############
LARGURA_JANELA = 550
ALTURA_JANELA = 510
TAMANHO_IMAGEM = (238,238)
TAMANHO_ICONE = (40,40)
IMAGENS_TK = []
X_INICIAL = 375
Y_INICIAL = 10
ESPACO_ENTRE_IMAGENS = 55

#######--------------####### Criando Janela #######--------------#######
titulo_janela = "POKEDEX POKEMON"
janela = criar_janela(titulo_janela,LARGURA_JANELA, ALTURA_JANELA)

#######--------------####### Criando o Frame Dados Pokemon #######--------------#######
frame_pokemon = Frame(janela, width=550, height=290, relief="groove", bg=pokemons["Pikachu"]["Tipo"]["cor"])
frame_pokemon.grid(row=1, column=0)

def trocar_pokemon(nome):
    ############## Cor Fundo Frame
    frame_pokemon["bg"] = pokemons[nome]["Tipo"]["cor"]
    ############## Dados Pokemon
    poke_nome["text"] = nome
    poke_nome["bg"] = pokemons[nome]["Tipo"]["cor"]
    poke_tipo["text"] = pokemons[nome]["Tipo"]["tipo"]
    poke_tipo["bg"] = pokemons[nome]["Tipo"]["cor"]
    poke_id["text"] = pokemons[nome]["Tipo"]["id"]
    poke_id["bg"] = pokemons[nome]["Tipo"]["cor"]
    ############## Imagem Pokemon 
    imagem_pokemon = carregar_imagem(pokemons[nome]["Tipo"]["imagem"], TAMANHO_IMAGEM)
    poke_imagem.config(image=imagem_pokemon, bg=pokemons[nome]["Tipo"]["cor"])
    poke_imagem.image = imagem_pokemon

    poke_tipo.lift()
    ############## Pokemon Status
    labels = [poke_hp, poke_ataque, poke_defeza, poke_velocidade, poke_total]

    for label, texto in zip(labels, pokemons[nome]["Status"].values()):
        label["text"] = texto
    ############## Pokemon Habilidades
    poke_habilidade1["text"] = pokemons[nome]["Habilidades"]["habilidade1"]
    poke_habilidade2["text"] = pokemons[nome]["Habilidades"]["habilidade2"]
    
############## Nome Pokemon ##############
poke_nome = Label(frame_pokemon, text="Pikachu", relief="flat", anchor=CENTER, font=("Fixedsys 20"), bg=co0, fg=co1)
poke_nome.place(x=12, y=15)

############## Tipo Pokemon ##############
poke_tipo = Label(frame_pokemon, text="Elétrico", relief="flat", anchor=CENTER, font=("Ivy 10"), bg=co0, fg=co1)
poke_tipo.place(x=12, y=50)

############## ID Pokemon ##############
poke_id = Label(frame_pokemon, text="#025", relief="flat", anchor=CENTER, font=("Ivy 10"), bg=co0, fg=co1)
poke_id.place(x=12, y=75)

#######--------------####### Imagem Pokemon #######--------------#######
poke_imagem = Label(frame_pokemon, relief="flat", bg=co0, fg=co1)
poke_imagem.place(x=60, y=50)

#######--------------####### Status Pokemon #######--------------#######
poke_status = Label(janela, text="Status", relief="flat", anchor=CENTER, font=("Verdana 20"), bg=co1, fg=co0)
poke_status.place(x=15, y=310)

############## HP Pokemon ##############
poke_hp = Label(janela, text="HP: 300", relief="flat", anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co2)
poke_hp.place(x=15, y=360)

############## Ataque Pokemon ##############
poke_ataque = Label(janela, text="Ataque: 600", relief="flat", anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co2)
poke_ataque.place(x=15, y=385)

############## Defeza Pokemon ##############
poke_defeza = Label(janela, text="Defeza: 500", relief="flat", anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co2)
poke_defeza.place(x=15, y=410)

############## Velocidade Pokemon ##############
poke_velocidade = Label(janela, text="Velocidade: 300", relief="flat", anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co2)
poke_velocidade.place(x=15, y=435)

############## Total Pokemon ##############
poke_total = Label(janela, text="Total: 1.700", relief="flat", anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co2)
poke_total.place(x=15, y=460)

#######--------------####### Habilidades Pokemon #######--------------#######
poke_habilidades = Label(janela, text="Habilidades", relief="flat", anchor=CENTER, font=("Verdana 20"), bg=co1, fg=co0)
poke_habilidades.place(x=180, y=310)

############## Habilidade 1 Pokemon ##############
poke_habilidade1 = Label(janela, text="Choque do Trovão", relief="flat", anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co2)
poke_habilidade1.place(x=195, y=360)

############## Habilidade 2 Pokemon ##############
poke_habilidade2 = Label(janela, text="Cabeçada", relief="flat", anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co2)
poke_habilidade2.place(x=195, y=385)

#######--------------####### Criando Botões #######--------------#######

############## Imagem Cabeça Pokemon ##############
for i, (nome, dados) in enumerate(pokemons.items()):
    foto_cabeca_pokemon = carregar_imagem(dados["Tipo"]["imagem_cabeca"], TAMANHO_ICONE)
    IMAGENS_TK.append(foto_cabeca_pokemon)
    
    botao_poke = Button(janela, command=lambda nome=nome: trocar_pokemon(nome), image=foto_cabeca_pokemon, text=nome, width=150, relief="raised", overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=("Verdana 12"), bg=co1, fg=co0)
    botao_poke.place(x=X_INICIAL, y=Y_INICIAL + i * ESPACO_ENTRE_IMAGENS)

############## Trocar o Pokemon quando Abrir ##############
trocar_pokemon(sorteio_pokemon())

#######--------------####### Rodando a Janela #######--------------#######
janela.mainloop()