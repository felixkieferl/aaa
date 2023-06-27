import numpy as np
import io

with open("N16_f.txt", "r") as f:
    data_str = f.read()
    
for frame_data_str in data_str.split("\n\n"):
    frame_data = np.loadtxt(io.StringIO(frame_data_str), delimiter=",")

print(frame_data)