from random import randint

print("숫자 야구 게임을 시작합니다.")

random_numbers = []

while len(random_numbers) != 3:
    random_number = randint(1, 9)
    if random_number not in random_numbers:
        random_numbers.append(random_number)

while True:
    user_inputs = input("숫자를 입력해주세요 : ")

    user_numbers = []

    for user_input in list(user_inputs):
        user_numbers.append(int(user_input))

    strikes = 0
    contains = 0

    for user_number in user_numbers:
        if user_number in random_numbers:
            contains += 1

    for i in range(0, 3):
        if user_numbers[i] == random_numbers[i]:
            strikes += 1

    balls = contains - strikes

    result_message = ""

    if balls == 0 and strikes == 0:
        result_message += "아웃"

    if strikes != 0:
        result_message += str(strikes) + " 스트라이크 "

    if balls != 0:
        result_message += str(balls) + " 볼"

    print(result_message)

    if strikes == 3:
        break

print("축하합니다. 승리하였습니다.")
