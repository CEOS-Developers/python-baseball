from model.Numbers import Numbers


def checkNumbersType(numbers):
    if not isinstance(numbers, Numbers):
        raise ValueError("Numbers 객체의 인스턴스가 아닙니다.")


class Baseball:
    def __init__(self, random_numbers):
        checkNumbersType(random_numbers)
        self.random_numbers = random_numbers
        self.strikes = 0
        self.balls = 0

    def __count_strikes(self, user_numbers):
        checkNumbersType(user_numbers)
        strikes = 0
        for i in range(0, 3):
            if user_numbers.get(i) == self.random_numbers.get(i):
                strikes += 1
        self.strikes = strikes

    def __count_balls(self, user_numbers):
        checkNumbersType(user_numbers)
        contains = self.__count_contains(user_numbers)
        self.balls = contains - self.strikes

    def __count_contains(self, user_numbers):
        checkNumbersType(user_numbers)
        contains = 0
        for user_number in user_numbers:
            if user_number in self.random_numbers:
                contains += 1
        return contains

    def play(self, user_numbers):
        self.__count_strikes(user_numbers)
        self.__count_balls(user_numbers)

    def result(self):
        result_message = ""
        if self.balls == 0 and self.strikes == 0:
            result_message += "아웃"

        if self.strikes != 0:
            result_message += str(self.strikes) + " 스트라이크 "

        if self.balls != 0:
            result_message += str(self.balls) + " 볼"

        return result_message


