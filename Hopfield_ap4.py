import numpy as np
import random as rand
import io
from matplotlib import pyplot as plt



#Función de probabilidad
def p(s,w,O,n,m,T,N):
    
    DE=(2*s[n,m]-1)*(sum(sum(w[:,:,n,m]*s))-O[n,m])
    
    pi=np.exp(-DE/T)
    if pi<1:
        p=pi
    else:
        p=1
    return p

#Parámetros iniciales
N=20
T=1e-4
P=100

#Pratrón/ones almacenados
g=np.zeros([P,N,N])
for num in range(P):
    for i in range(N):
        for j in range(N):
            g[num,i,j]=rand.randrange(0,2)


#a
a=sum(sum(np.transpose(g)))/(N**2)

#Peso sináptico w
w=np.zeros([N,N,N,N])
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                if (i,j)==(k,l):
                    continue
                else:
                    w[i,j,k,l]+=sum((g[:,i,j]-a)*(g[:,k,l]-a))/(N**2)

#Umbral de disparo
O=sum(sum(w))/2


#Función de cambio de espín
def f(s,w,O,T,N):
    for i in range(N**2):
        n=rand.randrange(0,N)
        m=rand.randrange(0,N)
        
        pr=p(s,w,O,n,m,T,N)
        e=rand.uniform(0,1)
        
        if e<pr:
            s[n,m]=1-s[n,m]
    return s

#Tiempo en pMC
t=20
#Variable de patrones recordados
Pc=0

for n in range(P):
    s=np.copy(g[n])
    for i in range(t):
        si=f(s,w,O,T,N)
        s=si
    m=0
    for j in range(N):
        for k in range(N):
            m+=(g[n,j,k]-a[n])*(s[j,k]-a[n])
    m/=((N**2)*a[n]*(1-a[n]))
    
    if m>0.75:
        Pc+=1

with open('m_ap4.txt', 'a') as res:
    res.write(str(P)+", "+str(Pc)+"\n")










    