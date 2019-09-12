from model.Numbers import Numbers


def get_user_input():
    try:
        user_inputs = input("숫자를 입력해주세요 : ")
        numbers = []
        for user_input in list(user_inputs):
            numbers.append(converter(user_input))
        return Numbers(numbers)
    except (TypeError, ValueError) as error:
        print(error)
        return get_user_input()


def converter(user_input):
    try:
        return int(user_input)
    except ValueError:
        raise TypeError("숫자만 입력이 가능합니다.")
