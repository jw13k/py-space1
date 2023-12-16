import numpy as np
import matplotlib.pyplot as plt

def activation_function(z, y_i):
        if z > 0:
                y = 1
        elif z == 0:
                y = y_i;
        elif z < 0:
                y = -1
    
    return y

def sign_inversion(t):
        for i in range(len(t)):
                if t[i] == 1:
                        t[i] = -1
                elif t[i] == -1:
                        t[i] = 1
    
        return t
