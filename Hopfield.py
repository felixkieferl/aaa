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
P=4

#Pratrón/ones almacenados
g=np.zeros([P,N,N])


for num in range(P):
    with open(str(num)+".txt", "r") as f:
        data_str = f.read()
    
    for frame_data_str in data_str.split("\n\n"):
        frame_data = np.loadtxt(io.StringIO(frame_data_str), delimiter=",")
    g[num]=frame_data



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

#Condición inicial
aleat=False
defor=0
prcen=30

if aleat:
    s=np.zeros([N,N])
    for i in range(N):
        for j in range(N):
            s[i,j]=rand.randrange(0,2,1)
else:
    s=np.copy(g[defor])
    for v in range(int((N**2)*prcen/100)):
        x=rand.randrange(0,N)
        y=rand.randrange(0,N)
        s[x,y]=1-s[x,y]


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

fich=open('ising_data.dat','w')

#Tiempo total en pMC
t=20 
#Array de solapamientos
mt=np.zeros([t,P])

#Bucle principal
for i in range(t):
    m=np.zeros(P)
    for j in range(N):
        for k in range(N):
            m+=(g[:,j,k]-a)*(s[j,k]-a)
            if k==N-1:
                print(str(2*s[j,k]-1),file=fich)
            else:
                print(str(2*s[j,k]-1)+", ",end="",file=fich)
            
    
    m/=((N**2)*a*(1-a))
    mt[i]=m
    
    print("",file=fich)
                
    si=f(s,w,O,T,N)
    s=si

fich.close()

t_list=np.linspace(0,t-1,t)

for n in range(P):
    plt.scatter(t_list,mt[:,n],marker="x",label=str(n))
    plt.xlabel("t (pMC)")
    plt.ylabel("m(s)")
if P>1:
    plt.legend(loc="lower right")
plt.savefig("")

with open('m_0123_defor.txt', 'a') as res:
    res.write(str(T))
    for n in range(P-1):
        res.write(", "+str(mt[-1,n]))
    res.write(", "+str(mt[-1,P-1])+"\n")











    