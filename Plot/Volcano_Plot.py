import numpy as np
import matplotlib.pyplot as plt

def del_E(n, E_surf_nH, E_surf, E_H2):
    return 1/n * (E_surf_nH-E_surf - n/2 * E_H2)


n = 1
E_H2 = -1.164851668533423
Metal = np.array(["Ag","Au","Mo","Pt"])
Metal_E = np.array([-2369.251320050268532,-2127.526871266153194,-4365.795058538102239,-7687.143423162807267])
Metal_H_E = np.array([-2369.830342421368641,-2128.098453575051735,-4366.408591960806916,-7687.745893106200128])


result_arr = del_E(n, Metal_H_E, Metal_E, E_H2)

#with open("result_arr.txt", "a") as f:
    #print(result_arr, file=f)
print(result_arr)