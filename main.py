from Player import Player as p
from Dado import Dado as d

jogadores = []
posicoesIniciais = [[0,0],[0,5],[5,0],[5,5]]
dado = d()
jogadorDaVez = 1

for i in range(4):
    jogadores.append(p(i+1))
    jogadores[i].posi = posicoesIniciais[i]


while True:
    print(jogadorDaVez)

