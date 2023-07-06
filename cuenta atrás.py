import numpy as np
import random as rand
import io



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
N=30
T=1e-4
P=10

#Pratrón/ones
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
w=np.zeros([P,N,N,N,N])
O=np.zeros([P,N,N])
for num in range(P):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    if (i,j)==(k,l):
                        continue
                    else:
                        w[num,i,j,k,l]+=(g[num,i,j]-a[num])*(g[num,k,l]-a[num])/(N**2)

    #Umbral de disparo
    O[num]=sum(sum(w[num]))/2

#Condición inicial
s=np.zeros([N,N])
aleat=True
defor=0
prcen=30

for i in range(N):
    for j in range(N):
        s[i,j]=rand.randrange(0,2,1)



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

t=100
mt=[]

for i in range(t):
    num=int((99-i)/10)
    m=np.zeros(P)
    for j in range(N):
        for k in range(N):
            m+=(g[:,j,k]-a)*(s[j,k]-a)
            if k==N-1:
                print(str(2*s[j,k]-1),file=fich)
            else:
                print(str(2*s[j,k]-1)+", ",end="",file=fich)
            
    
    m/=((N**2)*a*(1-a))
    mt.append(m)
    
    print("",file=fich)
                
    si=f(s,w[num],O[num],T,N)
    s=si
    if i%10==0:
        print(num)

fich.close()

print(mt)










    