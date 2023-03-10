#Valor da Hipotenusa de um Triangulo Retangulo 
from math import pow, sqrt 
cataj = float(input ('Insira o valor do cateto adjacente do triangulo retangulo: '))
catop = float(input('Insira o valor do cateto oposto do triangulo retangulo: '))
hip = sqrt((pow(cataj, 2)+pow (catop, 2)))
print ('O comprimento da hipotenusa é {:.3f}' .format(hip))