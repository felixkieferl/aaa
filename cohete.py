import numpy as np

G=6.67e-11
MT=5.9736e24
ML=0.07349e24
dTL=3.844e8
w=2.6617e-6
RT=6.37816e6
RL=1.7374e6
h=60
pr0=11090/dTL

D=G*MT/(dTL**3)
mu=ML/MT

N=30000

def dy(y,t):
    r,a,pr,pa=y
    rc=(1+r**2-2*r*np.cos(a-w*t))**0.5
    Fr=(pa**2)/(r**3)-D*(r**-2+mu*(r-np.cos(a-w*t))/(rc**3))
    Fa=-D*mu*r*np.sin(a-w*t)/(rc**3)
    return np.array([pr,pa*r**-2,Fr,Fa])

def yh(f,y,t):
    k1=h*f(y,t)
    k2=h*f(y+k1/2,t+h/2)
    k3=h*f(y+k2/2,t+h/2)
    k4=h*f(y+k3,t+h)
    return y+(k1+2*k2+2*k3+k4)/6

fich=open('planets_data.dat','w')

y0=np.array([RT/dTL,(np.pi)/2,pr0,0])
y=y0

for i in range(N):
    t=i*h
    
    xc=y[0]*np.cos(y[1])
    yc=y[0]*np.sin(y[1])
    xL=np.cos(w*t)
    yL=np.sin(w*t)
    
    if i/60==int(i/60):
        
        print("0.0, 0.0",file=fich)
        print(str(xL)+", "+str(yL),file=fich)
        print(str(xc)+", "+str(yc),file=fich)
        print("",file=fich)
    
    y=yh(dy,y,t)
    
    
    
    
fich.close()