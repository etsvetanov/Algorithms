# https://www.interviewcake.com/free-weekly-coding-interview-problem-newsletter

import random


def shuffle(l):
    for i in range(len(l)):
        swap_index = random.randint(0, len(l) - 1)
        if swap_index != i:
            tmp = l[i]
            l[i] = l[swap_index]
            l[swap_index] = tmp

    return l


# [8, 3, 6, 4, 7, 5, 2, 6, 1, 2]

for j in range(10):
    a = [random.randint(1, 10) for i in range(10)]
    print('list:', a, end='')
    print('shuffled:', shuffle(a))
