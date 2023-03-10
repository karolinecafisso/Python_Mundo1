#Calcular area da parece e tinta necessaria
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura*largura 

print ('A area da parede é de {} metros quadrados e irá gastar {} litros de tinta para pinta-la' .format (area, area/2))
