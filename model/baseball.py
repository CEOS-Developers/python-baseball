def user_numbers(user_inputs):
    numbers = []
    for user_input in list(user_inputs):
        numbers.append(int(user_input))
    return numbers


def count_strikes(numbers, random_numbers):
    strikes = 0
    for i in range(0, 3):
        if numbers[i] == random_numbers[i]:
            strikes += 1
    return strikes


def count_contains(numbers, random_numbers):
    contains = 0
    for number in numbers:
        if number in random_numbers:
            contains += 1
    return contains


def count_balls(numbers, random_numbers, strikes):
    contains = count_contains(numbers, random_numbers)
    return contains - strikes


def message_builder(balls, strikes):
    result_message = ""
    if balls == 0 and strikes == 0:
        result_message += "아웃"

    if strikes != 0:
        result_message += str(strikes) + " 스트라이크 "

    if balls != 0:
        result_message += str(balls) + " 볼"

    return result_message
