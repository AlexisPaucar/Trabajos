
#Multiplicación de Matrices usando numpy

import numpy as np
A=np.array([[1,2],[3,4],[5,6]]) 
B=np.array([[1,2,3],[3,4,5]])
C=np.dot(A,B)
def Imprimir(A):
    print()
    for i in A:
        print("[ ",end="")
        for j in i:
            print("{}".format(j),end=" ")
        print("]")
    print()    
Imprimir(A) 
Imprimir(B)
Imprimir(C)

