while True:
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")
    print("5. 종료")
    
    choice = input("원하는 연산을 선택하세요 (1-5): ")

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))

        if choice == "1":
            result = num1 + num2
            print("결과: ", result)
        elif choice == "2":
            result = num1 - num2
            print("결과: ", result)
        elif choice == "3":
            result = num1 * num2
            print("결과: ", result)
        elif choice == "4":
            if num2 != 0:
                result = num1 / num2
                print("결과: ", result)
            else:
                print("0으로 나눌 수 없습니다.")
    elif choice == "5":
        print("계산기를 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 1부터 5까지의 숫자 중 하나를 선택하세요.")
