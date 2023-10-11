#랜덤 숫자 6개 추첨

import random

#추첨 함수 정의
def generate_lottery_numbers():
    return random.sample(range(1, 46), 6)  # 1 ~ 45까지의 숫자 중 6개를 무작위로 선택

# 추첨 결과를 보여주는 함수 정의
def display_lottery_numbers(numbers):
    print("추첨된 복권 번호: ", numbers)

# 추첨 실행
if __name__ == "__main__":
    print("추첨 프로그램을 실행합니다!")
    input("Enter를 누르면 번호가 추첨됩니다...")
    
    lottery_numbers = generate_lottery_numbers()  # 숫자 추첨
    display_lottery_numbers(lottery_numbers)  # 추첨된 번호 출력
