import pandas as pd
import matplotlib.pyplot as plt

# 파일 경로
file_path = '2023년11월_교통카드_통계자료.csv'

# CSV 파일을 읽기
df = pd.read_csv(file_path)

# 새로운 데이터프레임을 생성하여 사용
line1_stations = df[df['호선명'] == '1호선'].copy()

# 사용할 시간대 컬럼 선택
time_columns = ['07:00:00~07:59:59', '08:00:00~08:59:59', '09:00:00~09:59:59']

# 새로운 컬럼을 생성하고 계산
line1_stations['출근시간_승하차_합'] = line1_stations[time_columns[0]].str.replace(',', '').astype(int) + line1_stations[time_columns[1]].str.replace(',', '').astype(int)

# 필요한 컬럼만 선택
line1_stations = line1_stations[['지하철역', '출근시간_승하차_합']]

# 그래프 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'

# 결과 출력
print('[1호선]')
print(line1_stations[['지하철역', '출근시간_승하차_합']])

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(line1_stations['지하철역'], line1_stations['출근시간_승하차_합'], marker='o', linestyle='--', color='blue')
plt.xlabel('역명')
plt.ylabel('출근시간 승하차 합')
plt.title('2023년도 11월 1호선 출근시간 승하차 인원')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
