
a=int(input('Ingrese Intervalo Inferior:'))
b=int(input('Ingrese Intervalo Superior:'))
i=1
while a==b or a>b:
    print('Inserte Nuevamente los datos')
    a=int(input('Ingrese Intervalo Inferior:'))
    b=int(input('Ingrese Intervalo Superior:'))
    i=i+1

print('Ah ingresado {} veces incorrectas'.format(i))
    