from tkinter import *
from PIL import Image
from dados import pokemons
from utils.carregar_imagens import carregar_imagem
from utils.criar_janela import criar_janela
from utils.sorteio_pokemon import sorteio_pokemon
from utils.carregar_Label import carregar_label
from services.pokeapi import PokeAPI
from models.pokemons import Pokemon
from models.status import Status
from views.janela_principal import Janela_Principal

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

############## Função Trocar Pokemon ##############
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
    
#######--------------####### Criando o Frame Dados Pokemon #######--------------#######
frame_pokemon = Frame(janela, width=550, height=290, relief="groove", bg=pokemons["Pikachu"]["Tipo"]["cor"])
frame_pokemon.grid(row=1, column=0)

poke_nome = carregar_label(frame_pokemon, 12, 15, "Pikachu", "Fixedsys 20 bold", co0, co1) #Nome
poke_tipo = carregar_label(frame_pokemon, 12, 50, "Elétrico", "Ivy 10 bold", co0, co1) #Tipo
poke_id = carregar_label(frame_pokemon, 12, 75, "#025", "Ivy 10 bold", co0, co1) #ID

#######--------------####### Imagem Pokemon #######--------------#######
poke_imagem = carregar_label(frame_pokemon, 60, 50) #Imagem Pokemon

#######--------------####### Status Pokemon #######--------------#######
poke_status = carregar_label(janela, 15, 310, "Status", "Verdana 20 bold")
poke_hp = carregar_label(janela, 15, 360, "HP: 300") #HP
poke_ataque = carregar_label(janela, 15, 385, "Ataque: 600") #Ataque
poke_defeza = carregar_label(janela, 15, 410, "Defeza: 500") #Defeza
poke_velocidade = carregar_label(janela, 15, 435, "Velocidade: 300") #Velocidade
poke_total = carregar_label(janela, 15, 460, "Total: 1.700") #Total

#######--------------####### Habilidades Pokemon #######--------------#######
poke_habilidades = carregar_label(janela, 180, 310, "Habilidades", "Verdana 20 bold")
poke_habilidade1 = carregar_label(janela, 195, 360, "Choque do Trovão") #Habilidade 1
poke_habilidade2 = carregar_label(janela, 195, 385, "Cabeçada") #Habilidade 2

#######--------------####### Criando Botões #######--------------#######

############## Imagem Cabeça Pokemon ##############
for i, (nome, dados) in enumerate(pokemons.items()):
    foto_cabeca_pokemon = carregar_imagem(dados["Tipo"]["imagem_cabeca"], TAMANHO_ICONE)
    IMAGENS_TK.append(foto_cabeca_pokemon)
    
    botao_poke = Button(janela, command=lambda nome=nome: trocar_pokemon(nome), image=foto_cabeca_pokemon, text=nome, width=150, relief="raised", overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=("Verdana 12"), bg=co1, fg=co0)
    botao_poke.place(x=X_INICIAL, y=Y_INICIAL + i * ESPACO_ENTRE_IMAGENS)

############## Trocar o Pokemon quando Abrir ##############
trocar_pokemon(sorteio_pokemon())

api = PokeAPI()
pokemon = api.buscar("rattata")
print("---------------- Testes Gerais ----------------")
print(pokemon._nome)
print(pokemon._id)
print(pokemon._tipos)
print(pokemon._habilidades)
print(pokemon._altura)
print(pokemon._peso)
print(pokemon._descricao)
print(pokemon._geracao)
print(pokemon._status.total)
print("---------------- Teste Movimento ----------------")
for move in pokemon.movimentos:
    print(f"Nome: {move.nome}")
    print(f"Tipo: {move.tipo}")
    print(f"Categoria: {move.categoria}")
    print(f"Poder: {move.poder}")
    print(f"Precisão: {move.precisao}")
    print(f"PP: {move.pp}")
    print(f"Descrição: {move.descricao}")
    print("-" * 30)
print("---------------- Teste Habilidades ----------------")
for habili in pokemon.habilidades:
    print(habili.nome)
    print(habili.descricao)
print("---------------- Teste Tipos ----------------")
for tipo in pokemon.tipos:
    print(tipo.nome)
    print(tipo.cor)
    print(tipo.fraquezas)
    print(tipo.resistencias)
    print(tipo.imunidades)
print("---------------- Teste Evoluções ----------------")
for evo in pokemon.evolucoes:
    print(evo.nome)
    print(evo.metodo)
    print(evo.nivel)
    print("-" * 20)
print("---------------- Teste Evoluções ----------------")
print(pokemon.imagem._oficial)
print(pokemon.imagem._shiny)
#######--------------####### Rodando a Janela #######--------------#######
janela.mainloop()

#app = Janela_Principal()
#app.executar()