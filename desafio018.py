#Seno Cosseno e Tangente de um Angulo
from math import sin, tan, radians, cos 
ang = float (input('Insira um angulo: '))
convert = radians(ang)
print(convert)
sen = sin(convert)
coss = cos(convert)
tang = tan (convert)
print ('O angulo {} possui o seno {:.2f}, cosseno {:.2f} e tangente {:.2f} em radianos' .format(ang, sen, coss, tang))