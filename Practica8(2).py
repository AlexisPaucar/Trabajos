
import math
def DigitoIzquierda(n):
    while n>10:
        n=math.trunc(n/10)
    return n

x=int(input('Digite un número:'))
print('El primer dígito es:',DigitoIzquierda(x))

y=int(input('Digite un número:'))
print('El primer dígito es:',DigitoIzquierda(y))