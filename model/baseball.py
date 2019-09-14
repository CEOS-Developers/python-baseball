def count_strikes(user_num, rand_num):
    strikes = 0
    for i in range(3):
        if user_num[i] == rand_num[i]:
            strikes += 1
    return strikes


def count_balls(user_num, rand_num, strikes):
    balls = 0
    for un in user_num:
        if un in rand_num:
            balls += 1
    return balls - strikes


def get_result_msg(balls, strikes):
    result_msg = ""
    if balls == 0 and strikes == 0:
        result_msg = "아웃"
    if strikes != 0:
        result_msg += str(strikes) + " 스트라이크 "
    if balls != 0 :
        result_msg += str(balls) + " 볼 "
    return result_msg