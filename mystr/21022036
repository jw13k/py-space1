import random
import string

def generate_random_sentence(length=50):
    sentence = []
    for _ in range(length):
        # 랜덤알파벳
        letter = random.choice(string.ascii_letters)
        sentence.append(letter)
    return "".join(sentence)

#원하는 문자열의 길이를 입력
user_length = int(input("원하는 문자열의 크기를 입력하세요: "))

#문장 출력
generated_sentence = generate_random_sentence(user_length)
print(generated_sentence)
