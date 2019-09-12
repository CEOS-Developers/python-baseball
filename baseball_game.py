from model import random
from model.Baseball import Baseball
from view import output_view, input_view

output_view.start_message()
random_numbers = random.generate_numbers()
baseball = Baseball(random_numbers)

while True:
    user_numbers = input_view.get_user_input()

    baseball.play(user_numbers)
    result_message = baseball.result()

    output_view.game_result(result_message)

    if baseball.strikes == 3:
        break

output_view.end_message()
