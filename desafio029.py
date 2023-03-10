
speed=int(input('Digite a velocidade que você estava: '))
if speed<=80:
    print ('Você estava dentro do limite de velocidade')
else:
    speed = (speed-80)*7
    print ('Você ultrapassou a velocidade permitida. Sua multa será de R$ {:.2f} reais' . format(speed))