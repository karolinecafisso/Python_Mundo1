# ** potencia
# // divisão inteira
# % resto da divisão

print(5%2) #resto é 1
print(5//2) #2*2 é 4, logo, 2 é o resultado
print(5**2) #5^2 é 25

#Ordem pra realizar as operações
#()
# potencia ** 
# //, %, *, /
# + - 


nome = input('Qual é o seu nome: ')
print ('Prazer em te conhecer {:=^20}!' .format(nome)) #saida: =======Karol========!


n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
s= n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print ('A soma vale {}, o produto vale {} e a divisão vale {:.3f}' .format(s, m, d) , end=' ')
#end= ' ' para deixar os prints juntos 
#:.3f pra mudar pra float com 3 casas de precisão
print ('A divisão inteira vale {} e a potencia {}' .format(di, e))

print ('Teste 1 e testando \n enquanto eu \n quiser') #quebra a linha

