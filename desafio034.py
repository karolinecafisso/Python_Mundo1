#aumento salario

salary=int(input('Digite o valor do seu salario: '))
if salary<=1250:
    print('O aumento do seu salario foi de 15%, logo o valor atual é de R$ {:.2f}' .format(salary+(salary*0.15)))
else: 
    print ('O aumento do seu salario foi de 10%, logo o valor atual é de R$ {:.2f}' .format(salary+(salary*0.1)))