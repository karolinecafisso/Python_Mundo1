#Calculo Aluguel Carro

day = int (input ('Quantos dias o carro ficou alugado?'))
km = float (input('Quantos Km foram rodados?'))
print ('O valor a pagar é de R$ {:.2f} reais' .format((day*60)+(km*0.15)))
