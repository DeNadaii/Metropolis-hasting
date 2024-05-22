import random
import math

pi = math.pi
e = math.e

arrPontos = [-1,1]

def Xtil(Xzero, Xfinal, X):                                     #Xtil ta em função de x
    return Xzero + (((X)*(Xfinal - Xzero)))                     #X nesse caso é 0.3, mas sempre sera aleatorio
                                                         

def FDP(Xtil,Xzero):                                          
    #(1/(math.sqrt(2*pi)))*(e**(0.5*((Xtil/Xzero)**2)))         #essa FDP é um exemplo; FDP em funçao de Xtil
    return Xzero-(Xzero*((1-Xtil)**2))
    

count = 0

while True:
    alpha = random.uniform(0.0, 2.0)
    beta  = random.uniform(0.0, 2.0)

    Paux = alpha                                            #Probabilidade auxiliar
    X = beta                                                #variavel independente (extocastica)

    if Paux <= FDP(Xtil(arrPontos[0],arrPontos[1], X),arrPontos[0]):
        print("bom sorteio")
        print("xtil",Xtil(arrPontos[0],arrPontos[1], X))
        print("fdp",FDP(Xtil(arrPontos[0],arrPontos[1], X),arrPontos[0]))
    
    if count >= 10:
        break
    print(count)
    count += 1