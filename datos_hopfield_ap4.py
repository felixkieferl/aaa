import numpy as np
import io
from matplotlib import pyplot as plt

with open("m_ap42.txt", "r") as f:
    data_str = f.read()
    
for frame_data_str in data_str.split("\n\n"):
    frame_data = np.loadtxt(io.StringIO(frame_data_str), delimiter=",")
datos=frame_data


plt.plot(datos[:,0],datos[:,1]/datos[:,0])
plt.xlabel('P')
plt.ylabel('Pc/P')
plt.savefig("a")









    