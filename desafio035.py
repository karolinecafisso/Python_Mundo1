#retas e triangulos

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 =  float(input('Digite o valor da terceira reta: '))
if r1<=r2+r3 and r2< r1+r3 and r3< r1+r2:
    print('As retas podem formar um triangulo')
else:
    print('As retas acima não podem formar triangulo3')