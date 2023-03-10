#Fatiamento 

frase = 'Curso em Video Python'
frase[9:13]
len(frase) #tamanho da frase
frase.count('o') #conta quantas vezes tem a letra o minuscula
frase.count('o', 0, 13) #vai contar o's do 0 até o 13
frase.find('deo') # vai indicar a posição que se  encontra o 'deo'
frase.find('Android') #vai retornar -1, que indica que não encontrou, já que começa no 0
'Curso' in frase #existe 'Curso' em frase? True

#Transformação

frase.replace('Python' ,' Android') #onde tem 'Python vai substituir por 'Android'
frase.upper() #vai trocar oq for minusculo pra maiusculo
frase.lower() #mantem o minusculo e substitui o maiusculo por minusculo
frase.capitalize() #joga todos os caracteres minusculo, e só o primeiro fica maiusculo
frase.title() #analisa quantas palavras tem a string, vai colocar letra maiuscula em cada palavra
frase.strip() #remove os espaços a mais na string
frase.rstrip() #trata pela direita, removendo os ultimos espaços
frase.lstrip() #remove os espaços da esquerda

#Divisão 

frase.split() #ele divide a string nos espaços, cada palavra gera uma lista

#Junção

'-'.join(frase) #reverte o split e coloca o -, se quiser espaço só fazer ' '


