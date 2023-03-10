#ler o nome completo, mostra o primeiro nome e o ultimo separadamente

nome = input ('Digite o seu nome completo: ').strip()
nome = nome.split()
print(nome[0], nome[len(nome)-1])