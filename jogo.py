import time
import os
import random


os.system("cls")
opcoes=["pedra","papel","tesoura"]
print("*"*100)
texto="Este é o jogo Pedra, Papel, Tesoura"
print(texto.center(100))
print("*"*100)

time.sleep(2)
os.system("cls")


print("Opções : 1.Pedra , 2.Papel, 3.Tesoura")

jog1=int(input("Entre com a sua opção: "))

if jog1==1:
    jogador1="Pedra"
elif jog1==2:
    jogador1="Papel"
elif jog1==3:
    jogador1="Tesoura"

jogale=random.randint(1,3)
jogador2=""

if jogale==1:
    jogador2="Pedra"
elif jogale==2:
    jogador2="Papel"
elif jogale==3:
    jogador2="Tesoura"
    
print(f'Jogador 1:{jogador1}')
print(f'Jogador 2:{jogador2}')
print("\n")

if jogador1==jogador2:
    print(" Jogo empatado")
if jogador1=="Pedra" and jogador2=="Tesoura"  or jogador1=="Papel" and jogador2=="Pedra" or jogador1=="Tesoura" and jogador2=="Papel":
    print("Jogador 1 Venceu")
else:
    print("Jogador 2 venceu")


resultado = "Jogador 1 venceu!"

