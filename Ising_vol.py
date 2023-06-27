import numpy as np
import random as rand

#Función p con condiciones de contorno periódicas


def DeltaE(s,n,m,N):
    if n==N-1:
        a=1
        b=N-2
    elif n==0:
        a=1
        b=N-2
    else:
        a=n+1
        b=n-1
    
    if m==N-1:
        c=1
        d=N-2
    elif m==0:
        c=1
        d=N-2
    else:
        c=m+1
        d=m-1
    
    DE=2*s[n,m]*(s[a,m]+s[b,m]+s[n,c]+s[n,d])
    return DE

def p(DE,T):
    pi=np.exp(-DE/T)
    if pi<1:
        p=pi
    else:
        p=1
    return p



N=16
T=1.6
s=np.ones([N,N])

def f(s,T,N):
    for i in range(N**2):
        n=rand.randrange(0,N)
        m=rand.randrange(0,N)
        
        DE=DeltaE(s,n,m,N)
        pr=p(DE,T)
        e=rand.uniform(0,1)
        
        if e<pr:
            s[n,m]=-s[n,m]
    return s
    

t=1000000

m_N=[]
E_S=[]
E_S2=[]
fi=np.zeros([N-1,N,N])
x=0

for i in range(t):
        
    if i/100==int(i/100):
        x+=1
        m=0
        Es=0
        e=0        
        for j in range(N):
            for k in range(N):
                m+=s[j,k]
                Es-=DeltaE(s,j,k,N)
                for l in range(1,N):
                    if j+l>N-1:
                        jl=j+l-N
                    else:
                        jl=j+l
                    fi[l-1,j,k]+=s[j,k]*s[jl,k]
                
                
        m_N.append(abs(m/(N**2)))
        E_S.append(Es/4)
        E_S2.append((Es/4)**2)
        
        
    
                
    si=f(s,T,N)
    s=si

    
mN=sum(m_N)/x

ES=sum(E_S)/x
ES2=sum(E_S2)/x

eN=ES/(2*N)

cN=(ES2-ES**2)/(T*N**2)



fi=fi/(x*N**2)
f=[]
for i in range(N-1):
    f.append(sum(sum(fi[i])))

with open('N'+str(N)+'.txt', 'a') as res:
    res.write(str(T)+", "+str(mN)+", "+str(eN)+", "+str(cN)+"\n")
    
with open('N'+str(N)+'_f.txt', 'a') as res:
    res.write(str(T)+", ")
    for i in range(len(f)):
        if i==len(f)-1:
            res.write(str(f[i])+"\n")
        else:
            res.write(str(f[i])+", ")











