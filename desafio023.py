#Ler um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

num = input('Digite um numero entre 0 e 9999: ')
print('O numero possui: \n Unidade: {} \n Dezena: {} \n Centena: {} \n Milhar: {}' .format(num[3], num[2], num[1], num[0]))