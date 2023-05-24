import numpy as np
import matplotlib.pyplot as plt



N=1000
nc=20
lm=0.3
T=1000
h=1

x=[]
for j in range(N+1):
    x.append(j*h)

x0=N*h/4
sg=N*h/16
k0=2*np.pi*nc/N
s=0.25*k0**-2


#Potencial
V=np.zeros(N+1,dtype = 'complex_')

for j in range(N+1):
    if 2*N/5<j<3*N/5:
        V[j]=lm*k0**2


#Función de onda en el instante t=0
ph0=np.zeros(N+1,dtype = 'complex_')

for j in range(1,N):
    if j==0 or j==N:
        continue
    ph0[j]=np.exp(k0*j*1j-(8*(4*j-N)**2)/(N**2))

ph0=ph0/(sum(ph0.real**2+ph0.imag**2)**0.5)

#Alfa
A0=-2+2j/s-V
a=np.zeros(N+1,dtype = 'complex_')

for j in range(3,N+1):
    a[-j]=1/(-A0[1-j]-a[1-j])

gm=1/(A0+a)                         #Gamma
ph=ph0

def betha(ph):
    B=np.zeros(N+1,dtype = 'complex_')
    b=4j*ph/s
    for j in range(3,N+1):
        B[-j]=gm[1-j]*(b[1-j]-B[1-j])
    return B


#Bucle principal
fich=open('schrodinger_data.dat','w')    
P=[]
for n in range(1,T):
    B=betha(ph)
    X=np.zeros(N+1,dtype = 'complex_')
    for j in range(1,N):
        X[j]=a[j-1]*X[j-1]+B[j-1]
    ph=X-ph
    re=(ph.real)**2
    im=(ph.imag)**2
    mph=re+im
    P.append(sum(re+im))
    for i in range(N+1):
        print(str(x[i])+", ",end="",file=fich)
        print(str(mph[i])+", ",end="",file=fich)
        print(str(re[i])+", ",end="",file=fich)
        print(str(im[i]),file=fich)
        #print(str((V.real[i])**2),file=fich)
    print("",file=fich)


fich.close()

plt.plot(np.linspace(2,1000,999),P)
plt.ylim(0,1.5)
plt.title('Probabilidad total')
plt.show()































    