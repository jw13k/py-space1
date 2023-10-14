import random

def guess_number():
    target_number = random.randint(1, 100)
    attempts = 0

    print("숫자 맞추기 게임을 시작 1부터 100 사이의 숫자를 맞춰보시오.")

    while True:
        user_guess = int(input("추측한 숫자를 입력하세요: "))
        attempts += 1

        if user_guess < target_number:
            print("UP.")
        elif user_guess > target_number:
            print("DOWN.")
        else:
            print(f"성공 {target_number}를 맞췄다. {attempts}번 시도하셨습니다.")
            break

guess_number()
