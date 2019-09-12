def checkType(numbers):
    if type(numbers) is not list:
        raise TypeError("배열만 가능합니다.")


def checkLength(numbers):
    if len(numbers) != 3:
        raise ValueError("적절한 길이가 아닙니다.")


def checkDuplicate(numbers):
    if len(set(numbers)) != 3:
        raise ValueError("중복된 값이 있습니다.")


class Numbers:
    def __init__(self, numbers):
        checkType(numbers)
        checkLength(numbers)
        checkDuplicate(numbers)
        self.size = len(numbers)
        self.numbers = numbers

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= self.size:
            raise StopIteration

        n = self.numbers[self.index]
        self.index += 1
        return n

    def get(self, index):
        return self.numbers[index]





