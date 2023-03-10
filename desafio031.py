
dist=int(input('Digite a distância da viagem em kilômetros:  '))
if dist<=200:
    print('O valor da passagem é R$ {:.2f} reais' .format(dist*0.5))
else:
    print('O valor da passagem é R$ {:.2f} reais' .format(dist*0.45))