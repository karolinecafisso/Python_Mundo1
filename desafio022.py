#Ler o nome completo e mostrar o nome com letra maiuscula, minusculas, quantas letras, quantas letras tem o primeiro nome

nome = input('Digite o seu nome completo: ')
print(nome.upper())
print(nome.lower())
print(len(nome))
nome = nome.split()
print(len(nome[0]))
