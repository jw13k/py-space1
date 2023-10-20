import csv
import matplotlib.pyplot as plt
import random

def display_chart(x_data, data, data2):

    plt.plot(x_data, data)
    plt.plot(x_data, data2)
    plt.show()

def display_bar_chart(x_data, data,data2):
    plt.barh(x_data, data)
   #plt.bar(x_data,data2)
    plt.show()
def get_data():
    check_text = "전국  (0000000000)"

    file = open('gend.csv','r', encoding='utf-8')
    csv_data = csv.reader(file)


    data =[]
    temp_data = []
    x_data =range(0, 101)

    for line in csv_data:
        if line[0] == check_text:
            temp_data = line[3:]

    for cur_data in temp_data:
        num = int(cur_data.replace(',',''))
        data.append(num)
        #print(num)
        #print(int[i])
        #data[i] = int(data[i])

    data2 = []

    for i in x_data:
        if i < 20:
            data2.append( data[0])
        else:
            data2.append(data[i-20])


    return{
        'x_data': x_data,
        'data': data,
        'data2': data2
    }




#end-def
result = get_data()
#print(result['x_data'])
#print(result['data'])
#display_chart(result['x_data'], result['data'],result['data2'])
display_bar_chart(result['x_data'], result['data'],result['data2'])
