import numpy as np
import matplotlib.pyplot as plt

m=(np.array([1.99e30,3.28e23,4.83e24,5.98e24,6.40e23,1.90e27,5.98e26,8.67e25,1.05e26]))/(1.99e30)
r0=np.array([[0,0],[5.79e10,0],[1.08e11,0],[1.496e11,0],[2.28e11,0],[7.78e11,0],[1.43e12,0],[2.87e12,0],[4.5e12,0]])/(1.496e11)
v0=np.array([[0,0],[0,47870],[0,35020],[0,29440],[0,24130],[0,13070],[0,9670],[0,6840],[0,5480]])*((1.496e11/(6.67e-11*1.99e30))**0.5)

#Nombre de los astros
nom=["Sol","Mercurio","Venus","Tierra","Marte","Júpiter","Saturno","Urano","Neptuno"]

dv=np.random.uniform(-0.01,0.01,(9,2))
dv[0]=[0,0]


def cuadr(r):                               #Función para saber el cuadrante en donde se encuentra el planeta en el plano XY
    cuad=np.zeros(8)
    for i in range(1,9):
        if r[i,0]>0:
            if r[i,1]>0:
                cuad[i-1]=1
            elif r[i,1]<0:
                cuad[i-1]=4
            else:
                cuad[i-1]=0.5
    return cuad


def mod(r):                                 #Función módulo de un vector
    return (r[0]**2+r[1]**2)**0.5


a=np.zeros([9,2])
for i in range(9):
    for j in range(9):
        if i==j:
            continue
        a[i]+=-m[j]*(r0[i]-r0[j])/((mod(r0[i]-r0[j]))**3)

h=0.01
v=v0+dv
r=r0

fich=open('planets_data.dat','w')

E=[]
tE=[]
cuad=cuadr(r)
p=[[0],[0],[0],[0],[0],[0],[0],[0]]


for n in range(200000):
    t=n*h
    r+=h*v+0.5*a*h**2
    w=v+h*a/2
    a=np.zeros([9,2])
    for i in range(9):
        for j in range(9):
            if i==j:
                continue
            a[i]+=-m[j]*(r[i]-r0[j])/((mod(r[i]-r[j]))**3)
    v=w+h*a/2
    
    if n/500==int(n/500):
        for k in range(9):
            print(str(r[k,0])+", "+str(r[k,1]),file=fich)
        print("",file=fich)  
    
    H=np.zeros(9)
    for l in range(9):
        H[l]+=0.5*m[l]*mod(v[l])**2
        for s in range(9):
            if s==l:
                continue
            H[l]-=m[l]*m[s]/(mod(r[l]-r[s]))
    
    for j in range(8):
        if cuad[j]==4:
            if cuadr(r)[j]==1:
                p[j].append(t-h/2)
            if cuadr(r)[j]==0.5:
                p[j].append(t)
    
    cuad=cuadr(r) 
    

    E.append(H)
    tE.append(t)

fich.close()


Et=sum(np.transpose(E))
Em=np.ones(len(Et))*sum(Et)/len(Et)

plt.plot(tE,Em)
plt.plot(tE,Et)
plt.show()        

#Periodos
T=[]
P=[[],[],[],[],[],[],[],[]]
d=[]

for k in range(8):
    if len(p[k])==1:
        T.append(0)
        d.append(0)
        P[k].append(0)
        plt.plot(P[k],label=nom[k+1])
        plt.show
        continue
    for l in range(1,len(p[k])):
        P[k].append(p[k][l]-p[k][l-1])
    d.append(np.std(P[k]))
    T.append(p[k][-1]/(len(p[k])-1))
    plt.plot(P[k])
    plt.show()
