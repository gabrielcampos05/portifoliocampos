#Atividades sobre importação
#Atividade 16

#Importa a biblioteca
import math

n=float(input('Digite um numero:'))

#trunc pega somente a parte inteira de um numero real
int=math.trunc(n)

print(f'O numero {n} tem a parte inteira {int}')

###########################################
#Atividade 17

catop=float(input('Digite o cateto oposto:'))

catadj=float(input('Digite o cateto adjacente:'))

hip=((catop**2)+(catadj**2))

delta=math.sqrt(hip)

print(f'O comprimento da hipotenusa eh:{delta}')

############################################
#Atividade 18

z=float(input('Digite um angulo:'))

seno=math.sin(z)
cosseno=math.cos(z)
tangente=math.tan(z)

print(f'Seno={seno} // Cosseno{cosseno} // Tangente:{tangente}')
