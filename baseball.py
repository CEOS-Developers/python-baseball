from random import randint

print("숫자 야구 게임을 시작합니다.")
rand_num = []
while len(rand_num) < 3:
    rand = str(randint(1, 9))
    if not rand in rand_num:
        rand_num.append(str(rand))

while True :

    user_num = list(input("숫자를 입력해주세요 : "))

    strikes = 0
    balls = 0

    for un in user_num:
        if un in rand_num:
            balls += 1

    for i in range(3):
        if user_num[i] == rand_num[i]:
            strikes += 1

    balls -= strikes

    result_msg = ""

    if balls == 0 and strikes == 0:
        result_msg = "아웃"
    if strikes != 0:
        result_msg += str(strikes) + " 스트라이크 "
    if balls != 0 :
        result_msg += str(balls) + " 볼 "

    print(result_msg)

    if strikes == 3:
        print("축하합니다. 승리하였습니다.")
        break