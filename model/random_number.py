from random import randint

def gen_rand_num():
    rand_num = []
    while len(rand_num) < 3:
        rand = str(randint(1, 9))
        if not rand in rand_num:
            rand_num.append(str(rand))
    return rand_num