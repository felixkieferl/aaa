import numpy as np
import random as rand
import funcion

#Función p con condiciones de contorno periódicas

N=16
T=1.6
t=100000

mN,eN,cN,f=funcion.simulacion_ising(N,T,t)

with open('N'+str(N)+'.txt', 'a') as res:
    res.write(str(T)+", "+str(mN)+", "+str(eN)+", "+str(cN)+"\n")
    
with open('N'+str(N)+'_f.txt', 'a') as res:
    res.write(str(T)+", ")
    for i in range(len(f)):
        if i==len(f)-1:
            res.write(str(f[i])+"\n")
        else:
            res.write(str(f[i])+", ")












