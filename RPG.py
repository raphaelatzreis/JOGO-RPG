from random import randint
from rich import print
from rich.console import Console
from rich.traceback import install
install()

#=========================
#CRIANDO OS PERSONAGENS
#=========================
print("✦•┈๑⋅⋯ Bem-vindo à Batalha no Terminal ⋯⋅๑┈·✦")
print("-----Crie os seus 2 personagens-----")
print("⋯⋅Mago ou Guerreiro⋯⋅")

lista_jogadores=[]

# ➤ CLASSE BASE
class Personagem:
    def __init__(self,nome,vida):
        self.nome = nome
        self.__vida = vida #ENCAPSULAMENTO: atributo privado
        
    #GETTER: permite ler vida
    def get_vida(self):
        return self.__vida
    
    
    #SETTER: aplica regras ao modificar a vida
    def set_vida(self,valor):
        if valor < 0:
            self.__vida = 0
        elif valor > 100:
            self.__vida = 100
        else:
            self.__vida=valor
            
    #PROPERTY: forma  de chamar get/set
    vida = property(get_vida,set_vida)
    
    
    def atacar(self): # ➤ MÉTODO
        print(f"{self.nome} realizou um ataque!")
        
class Guerreiro(Personagem):# ➤ CLASSE FILHA (1)
    def __init__(self,nome,vida,forca):
        super().__init__(nome,vida)
        self.forca = forca
    
    def atacar(self):
        dano_causado = self.forca - randint(0,20)
        print(f"{self.nome} realizou um ataque com a espada e causou {dano_causado} de dano.")
        return max(0,dano_causado) #garante que o dano não seja um número negativo
    
class Mago(Personagem):# ➤ CLASSE FILHA (2)
    def __init__(self,nome,vida,mana):
        super().__init__(nome,vida)
        self.mana = mana
        
    def atacar(self):
        dano_causado = self.mana - randint(0,20)
        print(f"O {self.nome} lançou um feitiço e causou um dano de {dano_causado}")
        return max(0,dano_causado) #garante que o dano não seja um número negativo
    
for q in range(0,2):
    print("=========================")
    print("CRIANDO OS PERSONAGENS")
    print("=========================")
    classePersonagem = int(input('Digite [1] - GUERREIRO \nDigite [2] - MAGO\n'))

    
    if classePersonagem == 1:
        nome = str(input("Digite o nome do seu personagem: "))
        forca = int(input(f"{nome} possui Força: "))
        vida = int(input(f"{nome} possuirá vida: "))
        jogador = Guerreiro(nome,vida,forca)
        lista_jogadores.append(jogador)
    
    
    elif classePersonagem == 2:
        nome = str(input("Digite o nome do seu personagem: "))
        mana = int(input(f"{nome} possui Magia: "))
        vida = int(input(f"{nome} possuirá vida: "))
        jogador = Mago(nome,vida,mana)
        lista_jogadores.append(jogador)

    else:
        print("[red]OPÇÃO DE PERSONAGEM INVÁLIDA[/red]")

print("------------------------------\n")

jogador1 = lista_jogadores[0]
jogador2 = lista_jogadores[1]

print("⋆༺𓆩⚔𓆪༻⋆꧁⎝ 𓆩༺⚔️ ༻𓆪 ⎠꧂⋆༺𓆩⚔𓆪༻⋆")
print("======== [green]INÍCIO DA BATALHA[/green] ========")

print(f"{jogador1.nome} X {jogador2.nome}")

# =======================
# ||  LOOP DA BATALHA  ||
# =======================

while True:
    # ➤ TURNO DO 1º JOGADOR  
    if input(print(f"{jogador1.nome} deseja atacar [S/N]? ")) in "Ss":
        ataque=jogador1.atacar()
        jogador2.vida = jogador2.vida-ataque
        print(f"{jogador2.nome} sofreu um ataque e agora possui [{jogador2.vida}] de vida.")
        print("⚔  ⚔  ⚔"*10)
        
        if jogador2.vida <= 0:
            print(f"{jogador2.nome} está [red]MORTO![/red]\n {jogador1.nome} VENCEU A BATALHA!")
            break
    else:
        print(f"{jogador1.nome} passou a vez!")
    # ➤ TURNO DO 2º JOGADOR
    if input(print(f"{jogador2.nome} deseja atacar [S/N]? ")) in "Ss": #"Ss": propriedade que aceita tanto S quanto s como input.
        ataque = jogador2.atacar()
        jogador1.vida = jogador1.vida - ataque
        print(f"{jogador1.nome} sofreu um ataque e agora possui [{jogador1.vida}] de vida.")
        print("⚔  ⚔  ⚔"*10)
        
        if jogador1.vida <= 0:
            print(f"{jogador1.nome} está [red]MORTO![/red]\n {jogador2.nome} VENCEU A BATALHA!")
            break
        else:
            print(f"{jogador2} passou a vez!")
print("==================")
print("||  FIM DE JOGO  ||") 
print("==================")
