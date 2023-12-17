import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 한글 폰트 파일 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 파일 경로
file_path = '2023년11월_교통카드_통계자료.csv'

# 파일 읽기
df = pd.read_csv(file_path, thousands=',')

# 승차 및 하차 열 선택 (시간대별)
time_columns = df.columns[5:-1]

# 시간대별 승하차 합산
df['합계'] = df[time_columns].sum(axis=1)

# '호선명'과 '합계' 열 선택
df_result = df[['호선명', '합계']]

# '합계'를 기준으로 내림차순 정렬
df_result = df_result.sort_values(by='합계', ascending=False)

# 상위 5개 행 선택
df_top5 = df_result.head(6)
df_top5['호선명'] = df_top5['호선명'].astype(str)

# 콘솔 출력
print(df_top5)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(df_top5['호선명'], df_top5['합계'], marker='o', linestyle='--', color='red')
plt.title('상위 5개 지하철 역별 총 승하차 인원')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
