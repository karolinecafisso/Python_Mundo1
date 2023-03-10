#Ler o nome da cidade e dizer se começa com a palavra Santo

city = input('Digite o nome da sua cidade: ')
city = city.split()
print('Santo' in city[0])