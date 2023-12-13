import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

crime_data = pd.read_csv('경찰청_범죄 발생 장소별 통계.csv')

location_columns = ['아파트_연립다세대', '단독주택', '고속도로', '노상', '백화점', '슈퍼마켓', '편의점', '대형할인매장',
                    '상점', '시장_노점', '숙박업소_목욕탕', '유흥접객업소', '사무실', '공장', '공사장_광산', '창고',
                    '역_대합실', '지하철', '기타교통수단내', '흥행장', '유원지', '학교', '금융기관', '의료기관',
                    '종교기관', '산야', '해상', '부대', '구금장소', '공지', '주차장', '공중화장실', '피씨방', '기타']

for idx, crime_type in enumerate(crime_data['범죄대분류'].unique()):
    plt.figure(figsize=(10, 5))

    plt.bar(x=location_columns, height=crime_data[crime_data['범죄대분류'] == crime_type][location_columns].sum())
    plt.title(f'{crime_type}')
    plt.xlabel('장소')
    plt.ylabel('범죄수')
    plt.xticks(rotation=90)


    file_name = f'{crime_type}_crime_chart.png'
    plt.savefig(file_name)


    plt.show()
