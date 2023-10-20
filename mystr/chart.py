import csv
import random

import matplotlib.pyplot as plt
def display_chart(x_data, data, data2):

    plt.plot(x_data, data)
    plt.plot(x_data, data2)
    plt.show()
#

def display_bar_chart(x_data, data, data2):
    plt.plot(x_data, data)
    plt.plot(x_data, data2)
    plt.show()
#

def get_data():

    check_text = '전국 {0000000000}'

    file = open('exam1.csv', 'r', encoding='utf-8')
    csv_data = csv.reader(file)

    data = []
    temp_data = []
    x_data = range(0, 101)

    for line in csv_data:
        if line[0] == check_text:
            print(line)
            data = line[3:]


    i = 0
    for current_data in data:
        num = current_data.replace(',', '')
        print(current_data, num)


        #print(int(i))
        #data[i] = int(data[i])
#

def get_data():

    check_text = '전국 {0000000000}'

    f = open('exam1.csv', 'r', encoding='utf-8')
    csv_data = csv.reader(f)

    data = []
    temp_data = []
    x_data = range(0, 101)

    for line in csv_data:
        if line[0] == check_text:
            temp_data = line[3:]


    i = 0
    for cur_data in data:
        num = cur_data.replace(',', '')
        data.append(num)

    data2 = []

    for i in x_data:
        if i < 20:
            data2.append( data[0])
        else:
            data2.append(data[1-20])

    return {
        'x_data': x_data,
        'data' : data,
        'data2' : data2
    }


        #print(int(i))
        #data[i] = int(data[i])
#

result = get_data()
print(result['x_data'])
print(result['data'])
display_chart(result['x_data'], result['data'])
