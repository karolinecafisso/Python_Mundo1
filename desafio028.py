import random

rand = random.randint(0,5)
num = int(input('Digite um numero de 0 a 5: '))
if num==rand:
    print('Parabéns! Você acertou, o numero era {}!' .format(rand))
else:
    print('Você errou, o numero era {}. Tente novamente!' .format(rand))


