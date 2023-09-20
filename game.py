import time
import os
from unidecode import unidecode
from frames import *

def limparTerminal():
  os.system('cls')

# Animar frames
def animate(anim, delay):
  for f in anim:
    limparTerminal()
    print(f)
    if anim.index(f) == len(anim) - 1:
      delay = 2
    time.sleep(delay)

animate(introFrames, 1.5)
limparTerminal()
print(splashFrames[0])
time.sleep(2.5)

# Variáveis de história
janela = False
chave = False
chaveTrue = False
canAnswer = True
bau = False
fim = 0
faca = 0
cabide = 0

inv = []

# Salas do jogo
class sala:
  FRENTE = 0   # salas principais
  DIREITA = 1
  ATRAS = 2
  ESQUERDA = 3

  COOL = 4     # sub salas
  CAMA = 5
  JANELA = 6
  ARMARIO = 7
  MESA = 8
  PORTA = 9
  ESPELHO = 10
  BAU = 11
  CAIXA = 12
  BILHETE = 13
  FINAL = 14
  LUA = 15
  CASA = 16

room = sala.FRENTE  # Setar sala atual

# Jogo (Ciclar entre os frames baseados nos inputs)
while True:
  limparTerminal()
  print("\n" + roomFrame[room])

  invPrint = ""
  for item in inv:
    invPrint += '\033[0;30;47m' + "[" + item + "]" +'\033[0;37;40m' + " "
  if len(inv) > 0: print("Itens: " + invPrint)
  else: print("")
  choice = unidecode(input(">> ").lower().strip())
  
  # Olhar para os lados da sala
  if room >= 0 and room <= 3:
    room += (choice == "d") - (choice == "e")

    # Clamp
    if room < 0:
      room = sala.ESQUERDA
    if room > 3:
      room = sala.FRENTE

  # Interações
  if choice == "cool room": room = sala.COOL

  match room:
    case sala.FRENTE:
      if choice == "cama": room = sala.CAMA
      if choice == "janela": room = sala.JANELA

    case sala.DIREITA:
      if choice == "armario": room = sala.ARMARIO
      if choice == "mesa": room = sala.MESA

    case sala.ATRAS:
      if choice == "porta": room = sala.PORTA

    case sala.ESQUERDA:
      if choice == "espelho": room = sala.ESPELHO
      if choice == "bau": room = sala.BAU

    case sala.COOL:
      if choice == "cabide" and cabide == 1:
        roomFrame[sala.COOL] = changedFrame[17]
        cabide = 2
        inv.remove("cabide")

    case sala.CAMA:
      if choice == "travesseiro": roomFrame[sala.CAMA] = changedFrame[8]

    case sala.JANELA:
      if choice == "lua": 
        room = sala.LUA
      if choice == "casa": 
        room = sala.CASA
        
    case sala.ARMARIO:
      if choice == "caixa": room = sala.CAIXA
      if choice == "cabide" and cabide == 0:
        roomFrame[sala.ARMARIO] = changedFrame[13]
        cabide = 1
        inv.append("cabide")
        
    case sala.MESA:
      if choice == "chave": 
        roomFrame[sala.MESA] = changedFrame[1]
        if chave == False: inv.append("chave")
        chave = True
      if choice == "bilhete" or choice == "recado" or choice == "anotacao": 
        room = sala.BILHETE
        janela = True
        roomFrame[sala.JANELA] = changedFrame[0]
        roomFrame[sala.LUA] = changedFrame[18]
        roomFrame[sala.CASA] = changedFrame[19]

    case sala.PORTA:
      if choice == "machado" and chaveTrue == True and fim == 0:
        fim = 1
        inv.remove("machado")
        break
      if choice == "chave" and faca == 2:
        inv.remove('\033[31m'+"chave"+'\033[0;30;47m')
        break

    case sala.ESPELHO:
      if choice == "cleiton fletcher": roomFrame[sala.ESPELHO] = changedFrame[2]
      if choice == "chave" and faca == 2: 
        roomFrame[sala.ESPELHO] = changedFrame[10]
        if chaveTrue == False: inv.append('\033[31m'+"chave"+'\033[0;30;47m')
        chaveTrue = True
      if choice == "faca" and faca == 1: 
        roomFrame[sala.ESPELHO] = changedFrame[9] 
        if bau == False: roomFrame[sala.ESQUERDA] = changedFrame[11]
        else: roomFrame[sala.ESQUERDA] = changedFrame[12]
        inv.remove('\033[31m'+"faca"+'\033[0;30;47m')
        faca = 2
      
    case sala.BAU:
      if choice == "chave" and chave == True: 
        roomFrame[sala.BAU] = changedFrame[3]
        if faca < 2: roomFrame[sala.ESQUERDA] = changedFrame[4]
        else: roomFrame[sala.ESQUERDA] = changedFrame[12]
        if bau == False: inv.remove("chave")
        bau = True

    case sala.CAIXA:
      if choice == senha1 and canAnswer == True:
        roomFrame[sala.CAIXA] = changedFrame[5]
        canAnswer = False
      if choice == senha2 and canAnswer == True:
        roomFrame[sala.CAIXA] = changedFrame[7]
        fim = 2
        canAnswer = False
      if choice == "machado" and canAnswer == False:
        roomFrame[sala.CAIXA] = changedFrame[6]
        if chaveTrue == False: inv.append("machado")
        chaveTrue = True
      if choice == "faca" and canAnswer == False and fim == 2:
        roomFrame[sala.CAIXA] = changedFrame[6]
        if faca == 0: inv.append('\033[31m'+"faca"+'\033[0;30;47m')
        faca = 1

  # Voltar para as salas antigas
  if choice == "" or choice == "sair" or choice == "exit":
    if room > 3 and room < 7: room = sala.FRENTE
    if room > 6 and room < 9: room = sala.DIREITA
    if room == 9: room = sala.ATRAS
    if room > 9 and room < 12: room = sala.ESQUERDA
    
    if room == 12: room = sala.ARMARIO
    if room == 13: room = sala.MESA
    if room == 15: room = sala.JANELA
    if room == sala.CASA: room = sala.JANELA
    
# Finais
limparTerminal()
match fim:
  case 1:
    print(roomFrame[sala.FINAL])
  case 2:
    animate(fimAltFrames, 1)

if len(inv) > 0: 
  print("Itens: " + invPrint)
else: 
  print("")

input(">> ")