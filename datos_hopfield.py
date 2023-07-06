import numpy as np
import io
from matplotlib import pyplot as plt


with open("m_0123_defor.txt", "r") as f:
    data_str = f.read()
    
for frame_data_str in data_str.split("\n\n"):
    frame_data = np.loadtxt(io.StringIO(frame_data_str), delimiter=",")
datos=frame_data


for n in range(1,len(datos[0])):
    plt.plot(datos[:,0],datos[:,n],label=str(n-1))
plt.xlabel('T')
plt.ylabel('m(s)')
plt.legend(loc="upper right")
plt.savefig("a")