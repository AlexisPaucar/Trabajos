

def covertirCelciusaFahrenheit(celcius):
    Fahrenheit=(celcius*(180.0/100.0))+32;
    return Fahrenheit
    
Cel1=float(input('Ingrese los grados Celcius:'))
print('Fahrenheit:',covertirCelciusaFahrenheit(Cel1))

Cel2=float(input('Ingrese los grados Celcius:'))
print('Fahrenheit:',covertirCelciusaFahrenheit(Cel2))