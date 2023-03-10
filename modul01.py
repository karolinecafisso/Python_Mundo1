import math 

for name in dir(math): #dessa forma com o dir() podemos ver as entidades pertencentes ao modulo
    print(name, end="\t")


from math import ceil, trunc, floor 
x = 1.4
y = 2.6

print(floor(x), floor(y)) #pega o numero inteiro 1 e 2
print(floor(-x), floor(-y)) # pega o numero maior inteiro -2 -3
print(ceil(x), ceil(y)) #pega o numero maior inteiro 2 3
print(ceil(-x), ceil(-y)) #pega o numero inteiro -1 -2
print(trunc(x), trunc(y)) #pega a parte inteira 1 2
print(trunc(-x), trunc(-y)) #parte inteira negativa -1 -2

from random import randint 

for i in range(10):
    print(randint(1,10) , end=",") #sorteia 10 numeros, porém os numeros se repetem

from platform import platform 

print(platform()) #esse modulo mostra as informações do sistema
print(platform(1))
print(platform(0, 1))

from platform import machine

print(machine()) #essa função mostra o nome generico do processador


from platform import processor

print(processor()) #mostra o nome real do processador

from platform import system

print(system()) #mostra o nome genérico do sistema operacional Windows, Linux, Mac

from platform import version

print(version()) #versao do SO

from platform import python_implementation, python_version_tuple

print(python_implementation()) #mostra a implementação do python, CPython

for atr in python_version_tuple(): #saber a versão do python
    print(atr)


