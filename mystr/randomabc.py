import random
import string

def ge_random_sen(length=50):
    sentence = []
    for _ in range(length):
        letter = random.choice(string.ascii_letters)
        sentence.append(letter)
    return "".join(sentence)

gen_sen = ge_random_sen()
print(gen_sen)
