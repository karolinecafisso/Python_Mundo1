#ano bissexto

ano=int(input('Digite o ano para verificar se é bissexto: '))
if (ano%2)==0:
    print('O ano {} é bissexto!' .format(ano))
else:
    print('O ano {} não é bissexto!' .format(ano))