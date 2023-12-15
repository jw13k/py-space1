import random

import matplotlib.pyplot as plt
import numpy as np


#data = np.random.choice(45, 6, replace=False) + 1
#print(data)

data_rate = [0.1, 0.1, 0.6, 0.1, 0.1]
data = np.random.choice(5, 10000, p=data_rate)




print(data)
data_length = len(data_rate)
plt.hist(data, bins=data_length, color='r')
plt.show()

