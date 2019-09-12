from model import random, baseball
from view import output_view, input_view

output_view.start_message()

random_numbers = random.generate_numbers()

while True:
    user_inputs = input_view.get_user_input()

    user_numbers = baseball.user_numbers(user_inputs)

    strikes = baseball.count_strikes(user_numbers, random_numbers)
    balls = baseball.count_balls(user_numbers, random_numbers, strikes)

    result_message = baseball.message_builder()

    output_view.game_result(result_message)

    if strikes == 3:
        break

output_view.end_message()
