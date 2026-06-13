# ⚔️ Batalha no Terminal: RPG em Python

Um mini jogo de batalha RPG em turnos via linha de comando (terminal) desenvolvido 100% em Python. Este projeto foi criado com o objetivo de aplicar na prática os pilares fundamentais da **Programação Orientada a Objetos (POO)**.



## Objetivo do Projeto

O foco principal deste repositório é demonstrar a aplicação prática de:
* **Herança:** Criação de classes filhas (`Guerreiro` e `Mago`) a partir de uma classe base (`Personagem`).
* **Polimorfismo:** Métodos de ataque com comportamentos diferentes dependendo da classe escolhida.
* **Encapsulamento:** Proteção do atributo de `vida` dos personagens utilizando métodos *Getter*, *Setter* e a função `property`.
* **Interface via Terminal:** Uso da biblioteca `rich` para trazer cores e formatação ao console, melhorando a experiência do usuário.



## Como o jogo funciona

1. O jogo começa pedindo para o usuário criar dois personagens.
2. É possível escolher entre as classes **Guerreiro** (focado em Força) ou **Mago** (focado em Magia/Mana).
3. Após definir os nomes e os atributos de cada um, a batalha se inicia.
4. O combate acontece em turnos, onde cada jogador pode escolher se deseja atacar ou passar a vez.
5. O dano é calculado com base nos atributos do personagem somado a um fator de aleatoriedade (RNG).
6. O jogo termina quando a vida de um dos personagens chega a zero.


## Como executar na sua máquina

### Pré-requisitos
* Ter o [Python](https://www.python.org/downloads/) instalado na sua máquina (versão 3.x).
* Instalar a biblioteca `rich` para a formatação do terminal.

### Passo a passo

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/raphaelatzreis/JOGO-RPG.git](https://github.com/raphaelatzreis/JOGO-RPG.git)
