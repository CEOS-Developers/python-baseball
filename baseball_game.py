from model.baseball import count_strikes, count_balls, get_result_msg
from model.random_number import gen_rand_num
from view.outputview import *
from view.inputview import *

start_message()

rand_num = gen_rand_num()

while True :
    user_num = get_user_input()

    strikes = count_strikes(user_num, rand_num)
    balls = count_balls(user_num, rand_num, strikes)

    game_result(get_result_msg(balls, strikes))

    if strikes == 3:
        end_message() #outputview end_message
        break