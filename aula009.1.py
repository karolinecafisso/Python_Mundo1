frase = '   Curso em Video Python   '
print(frase.upper().count('o')) #contar quantos o tem na frase após deixar ela toda maiuscula

print(len(frase)) #tamanho da frase

print(len(frase.strip())) #tamanho da frase após juntar os espaços em brancos

print(frase.replace('Python' , 'Android')) #se fizer dessa forma, não salva a alteração
print (frase)

frase = frase.replace('Python' , 'Android') #dessa forma salva a alteraçao
print(frase)

print('Curso' in frase) #mostra se tem curso na frase
print(frase.title().find('Video')) #achar Video na frase 

print(frase.split())
dividido = frase.split() #transforma em lista
print (dividido[0]) #pega o primeiro elemento da lista
print (dividido [2][3]) #mostra a palavra 2, letra 3



# print("""Um caminho para desmistificar as carreiras em tecnologia é estimular que líderes
# # em TI ajam como modelo para jovens no processo de escolha da profissão. Mostrar que a mulher
# # compete e é bem sucedida nesse mercado é um incentivo para que mais jovens mulheres apostem
# # em carreiras de tecnologia como áreas de atuação profissional. Também é preciso incentivar
# # as escolas e instituições a adotarem políticas de diversidade e garantir espaços seguros para
# # que as mulheres possam se desenvolver nesses ambientes. Na matéria do Valor Empresas| 
# # Carreira de hoje, falo um pouco mais sobre isso""")