
n=int(input('Ingrese el Valor de n:'))
for i in range(1,n+1):
  res=0
  aux=1
  for j in range(1,i+1):
    res+=aux
    aux+=2;        
  print (f"{i}^2 = {res}")