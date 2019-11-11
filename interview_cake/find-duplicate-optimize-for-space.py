import random


def find_duplicate(a: list):
    # n = 10
    # 10
    # values in a are 1 <= x <= n
    size = len(a)
    n = size - 1

    ranges = {
        'low_left': 1,
        'high_left': n // 2,
        'low_right': n // 2 + 1,
        'high_right': n
    }

    while True:
        count_left = 0
        count_right = 0

        size_left = ranges['high_left'] - ranges['low_left'] + 1
        size_right = ranges['high_right'] - ranges['low_right'] + 1

        for x in a:
            if ranges['low_left'] <= x <= ranges['high_right']:
                count_left += 1
            else:
                count_right += 1

        if count_left > size_left:
            if size_left == 1:
                return ranges['low_left']
            # ranges['low_left'] stays the same
            ranges['high_left'] = ranges['low_left'] + size_left // 2 - 1
            ranges['low_right'] = ranges['low_left'] + size_left // 2
            ranges['high_right'] = ranges['low_left'] + size_left - 1
        else:
            if size_right == 1:
                return ranges['low_right']

            ranges['low_left'] = ranges['low_right']
            ranges['high_left'] = ranges['low_left'] + size_right // 2 - 1
            ranges['low_right'] = ranges['low_left'] + size_right // 2
            # ranges['high_right'] stays the same


hunderd = list(range(100))

test_1 = list(hunderd)
test_1.append(2)
random.shuffle(test_1)

test_2 = list(hunderd)
test_2.append(2)
test_2[50] = 90
test_2[89] = 90
random.shuffle(test_2)

print('find_duplicate(test_1):', find_duplicate(test_1))
assert find_duplicate(test_1) == 2
print('find_duplicate(test_2):', find_duplicate(test_2))
assert find_duplicate(test_2) in (2, 90)
