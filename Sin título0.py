import numpy as np
import matplotlib.pyplot as plt

#Constantes
G=6.67e-11
Ms=1.99e30
c=1.49e11
m=np.array([1.98e30, 3.28e23, 4.83e24, 5.98e24, 6.4e23, 1.9e27, 5.98e24, 8.67e25, 1.05e26])/Ms

#Arrays de posiciones y velocidades iniciales
r0=(np.array([[0,0], [5.79e10,0],[1.08e10,0],[1.49e11,0],[2.28e11,0],[7.78e11,0],[1.43e12,0],[2.87e12,0],[4.5e12,0]]))/c
v0=(np.array([[0,0],[0,47870],[0,35020],[0,29440],[0,24130],[0,13070],[0,9670],[0,6840],[0,5480]]))*(((c/(G*Ms)))**0.5)

#Funciones
def mod(r):                                 #Función módulo de un vector
    return (r[0]**2+r[1]**2)**0.5

def ah(m,r):                                #Función de aceleración
    a=np.zeros([9,2])
    for i in range(1,9):
        for j in range(0,9):
            if j==i:
                continue
            a[i]+=-m[j]*(r[i]-r[j])/(mod(r[i]-r[j])**3)
    return a

def rh(rt,vt,at,h):                         #Función de posición
    return rt+h*vt+0.5*at*h**2

def wh(vt,at,h):                            #Función w
    return vt+h*at/2

def vh(wh,ah,h):                            #Función de velocidad
    return wh +0.5*h*ah

def Eh(m,rt,vt):
    E=m[1:]*(v[1:,0]**2+v[1:,1]**2)/2-m[0]*m[1:]/((r[1:,0]**2+r[1:,1]**2)**0.5)
    return E

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

#Perturbaciones
dr=np.random.uniform(-0.05,0.05,(9,2))
dv=np.random.uniform(-0.01,0.01,(9,2))
dr[0]=[0,0]
dv[0]=[0,0]

tmax=(5.20344e9*(G*Ms/(c**3))**0.5)/100     #Tiempo total del programa en función de la órbita de Neptuno

n=1000                                      #Número de divisiones del tiempo
h=tmax/n                                    #Pasos de tiempo h

#Variables a usar definidas con su valor inicial (excepto para el tiempo)
t=h                                         #Tiempo
r=r0+dr                                     #Posición
v=v0+dv                                     #Velocidad
a=ah(m,r0)                                  #Aceleración
E=[Eh(m,r,v)]
tE=[0]
cuad=cuadr(r)

p=[[0],[0],[0],[0],[0],[0],[0],[0]]

#Bucle principal

fich=open('planets_data.dat','w')           #Fichero de salida

while t<tmax:
    r=rh(r,v,a,t)
    w=wh(v,a,t)
    a=ah(m,r)
    v=vh(w,a,t)
    t+=h
    E.append(Eh(m,r,v))
    tE.append(t)
    
    for i in range(9):
        print(str(r[i][0])+", "+str(r[i][1]),file=fich)
    
    for j in range(8):
        if len(p[j])>5:
            continue
        if cuad[j]==4:
            if cuadr(r)[j]==1:
                p[j].append(t-h/2)
            if cuadr(r)[j]==0.5:
                p[j].append(t)
    
    cuad=cuadr(r)    
            
    print("",file=fich)

fich.close()


#Repressentación de energías
Et=np.array(E)

for i in range(8):
    l=len(tE)
    for j in range(len(tE)):
       if Et[j,i]>0:
           l=j+1
           break
    plt.plot(tE[:l],Et[:l,i])
    plt.show()

#Lista de tiempos en los que cada planeta  da una vuelta
T=[]
for k in range(8):
    T.append(p[k][len(p[k])-1])



















