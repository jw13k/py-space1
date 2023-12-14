import tkinter as tk
from datetime import datetime

def show_current_time():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text="현재 시각: " + formatted_time)

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("현재 시각 표시")

# 라벨 생성 및 초기 설정
time_label = tk.Label(window, text="", font=("Helvetica", 16))
time_label.pack(pady=20)

# 버튼 생성 및 명령 설정
button = tk.Button(window, text="현재 시각 표시", command=show_current_time)
button.pack(pady=10)

# 종료 버튼 생성 및 명령 설정
exit_button = tk.Button(window, text="종료", command=window.destroy)
exit_button.pack(pady=10)

# Tkinter 이벤트 루프 시작
window.mainloop()
