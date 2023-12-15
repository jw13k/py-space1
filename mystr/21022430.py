import matplotlib.pyplot as plt
import numpy as np

def action1():
    range_data = range(0, 50, 2)
    data = []
    data_1 = []
    data_2 = []
    data_3 = []

    for i in range_data:
        data.append(i)
        data_1.append( (i / 10) * 1 )
        data_2.append( (i / 10) * 2 )
        data_3.append( (i / 10) * 3 )

    plt.plot(data, data_1, 'r--')
    plt.plot(data, data_2, 'bs')
    plt.plot(data, data_3, 'g^')
    plt.show()
#end-def

def action2():
    data = range(0, 50, 2)
    data_1 = np.arange(0., 5., 0.2)
    data_2 = data_1 * 2
    data_3 = data_1 * 3

    print(data_1)
    print(data_2)
    print(data_3)

    plt.plot(data, data_1, 'r--')
    plt.plot(data, data_2, 'bs')
    plt.plot(data, data_3, 'g^')
    plt.show()
#end-def

action2()
