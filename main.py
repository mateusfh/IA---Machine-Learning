from Player import Player
import random
import math

global terrain

def InitializeTerrain(lines, coluns):
    global terrain
    terrain = []
    for i in range(lines):
        aux = []
        for j in range(coluns):
            aux.append(0)
        
        terrain.append(aux)


def PrintTerrain():
    global terrain
    i = 0
    for i in terrain:
        print(i)
  

def RulesMoviment(move, line, colum):
    if move == 4:
        if colum == 0:
            return False
        return True

    elif move == 8:
        if line == 0:
            return False
        return True

    elif move == 2:
        if line == 2:
            return False
        return True

    elif move == 6:
        if colum == 2:
            return False
        return True

def Moviment(line, colum):
    move = int(input("Digite a direcao (4 - esq, 6 - dir, 8 - up, 2 - down): "))

    if(RulesMoviment(move, line, colum)):
        if move == 4:
            colum -= 1

        elif move == 8:
            line -= 1

        elif move == 2:
            line += 1

        elif move == 6:
            colum += 1
    
    return line, colum

def main():
    global terrain
    InitializeTerrain(3,3)
    
    linhaAtual = 0
    columAtual = 0

    terrain[0][0] = 1

    player = []

    linhaAnterior = 0
    columAnterior = 0

    while(1):
        PrintTerrain()
        linhaAnterior = linhaAtual
        columAnterior = columAtual
        linhaAtual, columAtual = Moviment(linhaAtual, columAtual)

        if linhaAtual != linhaAnterior or columAtual != columAnterior:
            terrain[linhaAtual][columAtual] = 1
            terrain[linhaAnterior][columAnterior] = 0




if __name__ == '__main__':
    main()