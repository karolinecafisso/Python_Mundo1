#Desconto Produto em 5%

valorp=float(input('Insira o valor do produto sem desconto: '))
print('O valor do produto atual é de R$ {} reais, e com 5% de desconto irá passar para R$ {:.2f} reais' .format(valorp, valorp-(valorp*0.05)))


#Aumento de 15% do Salário

salario=float(input('Insira o seu salário atual em carteira: '))
print ('O seu salário atual com o valor de R$ {:.2f} reais com 15% de aumento, mudou para R$ {:.2f}' .format(salario, salario+(salario*0.15)))