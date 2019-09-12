from random import randint

from model.Numbers import Numbers


def generate_numbers():
    random_numbers = []
    while len(random_numbers) != 3:
        random_number = randint(1, 9)
        if random_number not in random_numbers:
            random_numbers.append(random_number)
    return Numbers(random_numbers)
