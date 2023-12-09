import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_csv('경찰청_범죄 발생 시간대 및 요일.csv')

#00시-02시59분,03시-05시59분,06시-08시59분,09시-11시59분
time_columns = ['0시-2시59분', '3시-5시59분', '6시-8시59분', '9시-11시59분', '12시-14시59분', '15시-17시59분',
                '18시-20시59분', '21시-23시59분', '미상']
day_columns = ['일', '월', '화', '수', '목', '금', '토']

#색
colors = ['skyblue', 'skyblue', 'skyblue', 'skyblue', 'skyblue', 'skyblue', 'skyblue', 'skyblue', 'gray']

for idx, row in df.iterrows():
    crime_type = row['범죄대분류'] + '_' + row['범죄중분류']
    data = [row[time_col] for time_col in time_columns]

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.bar(time_columns, data, color=colors, label=crime_type)

    ax.set_title(f'{crime_type}')
    ax.set_xlabel('시간대')
    ax.set_ylabel('범죄 발생 건수')
    ax.legend()

    plt.show()
