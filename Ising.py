import numpy as np
import random as rand

def p(s,n,m,T,N):
    if n==N-1:
        i=0
        a=1
        b=N-2
    elif n==0:
        i=0
        a=1
        b=N-2
    else:
        i=n
        a=n+1
        b=n-1
    
    if m==N-1:
        j=0
        c=1
        d=N-2
    elif m==0:
        j=0
        c=1
        d=N-2
    else:
        j=m
        c=m+1
        d=m-1
    
    DE=2*s[i,j]*(s[a,j]+s[b,j]+s[i,c]+s[i,d])
    pi=np.exp(-DE/T)
    if pi<1:
        p=pi
    else:
        p=1
    return p

N=100
T=1
s=np.zeros([N,N])

for i in range(N):
    for j in range(N):
        s[i,j]=rand.randrange(-1,2,2)

def f(s,T,N):
    for i in range(N**2):
        n=rand.randrange(0,N)
        m=rand.randrange(0,N)
        
        pr=p(s,n,m,T,N)
        e=rand.uniform(0,1)
        
        if e<pr:
            s[n,m]=-s[n,m]
    return s

fich=open('ising_data.dat','w')

t=1000000

for i in range(t):
    for j in range(N):
        for k in range(N):
            if k==N-1:
                print(str(s[j,k]),file=fich)
            else:
                print(str(s[j,k])+", ",end="",file=fich)
    print("",file=fich)
            
    si=f(s,T,N)
    s=si

fich.close()