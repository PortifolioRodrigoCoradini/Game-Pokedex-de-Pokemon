# 📖 Pokédex Pokémon

Uma Pokédex desenvolvida em **Python** utilizando **Tkinter** e **Pillow**, que permite visualizar informações de diversos Pokémon de forma interativa.

## 📷 Demonstração

Gravando 2026-07-05 150816.gif

## ✨ Funcionalidades

- 🎲 Pokémon inicial escolhido aleatoriamente.
- 🔄 Troca de Pokémon através dos botões laterais.
- 🖼️ Exibição da imagem do Pokémon.
- 🎨 Mudança automática da cor de fundo conforme o tipo do Pokémon.
- 📊 Exibição dos atributos:
  - HP
  - Ataque
  - Defesa
  - Velocidade
  - Total
- ⚔️ Exibição das habilidades do Pokémon.
- 🖱️ Interface gráfica desenvolvida com Tkinter.


## 📂 Estrutura do Projeto

```
Game_Pokemon/
│
├── images/
│   ├── pikachu.png
│   ├── bulbasaur.png
│   ├── charmander.png
│   ├── gyarados.png
│   ├── gengar.png
│   ├── dragonite.png
│   
│
├── funcoes/
│   ├── carregar_imagens.py
│   ├── criar_janela.py
│   └── sorteio_pokemon.py
│
├── dados.py
├── main.py
└── README.md
```

---

## 🚀 Tecnologias Utilizadas

- Python 3
- Tkinter
- Pillow (PIL)
- Random

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/RodrigoCoradini-Ofic/Game-Pokedex-de-Pokemon
```

Entre na pasta:

```bash
cd Game_Pokemon
```
Instale as dependências:
```bash
pip install tkinter
pip install pillow
```
Execute o projeto:
```bash
python main.py
```

## 🎮 Como utilizar

Ao iniciar o programa:

- Um Pokémon é escolhido aleatoriamente.
- Clique em qualquer Pokémon da lista lateral.
- As informações serão atualizadas automaticamente:
  - Nome
  - Número da Pokédex
  - Tipo
  - Status
  - Habilidades
  - Imagem
  - Cor da interface

## 💻 Conceitos utilizados

Durante o desenvolvimento foram utilizados diversos conceitos da linguagem Python:

- Organização em módulos
- Funções reutilizáveis
- Dicionários aninhados
- Estruturas de repetição
- Estruturas de decisão
- Manipulação de imagens com Pillow
- Interface gráfica utilizando Tkinter
- Eventos e comandos de botões
- Geração aleatória com o módulo Random

## 📈 Melhorias Futuras

- [ ] Adicionar mais Pokémon
- [ ] Barra de pesquisa
- [ ] Sistema de favoritos
- [ ] Evoluções
- [ ] Sons ao trocar Pokémon
- [ ] Animações na troca de Pokémon
- [ ] Mostrar fraquezas e resistências
- [ ] Exibir peso e altura
- [ ] Barra gráfica para os atributos
- [ ] Modo escuro

## 👨‍💻 Autor

**Rodrigo Coradini**

GitHub:
https://github.com/RodrigoCoradini-Ofic

## ⭐ Sobre

Este projeto foi desenvolvido com o objetivo de praticar conceitos de programação em Python, manipulação de interfaces gráficas com Tkinter e organização de projetos em múltiplos módulos.

Além das funcionalidades básicas, o projeto também busca oferecer uma interface agradável e organizada, servindo como material de estudo e para compor meu portfólio no GitHub.