from typing import List, Dict

start = 2

# find min1, min2 -> O(n)
# n + (n-1) + (n-2) + ... + 1 = n(n+1) / 2 <> nnlogn
numbers = []
numbers.sort()

while True:
    # O(n(nlog(n)))
    numbers = [numbers[0] + numbers[1], ...[numbers[2:]]]
    numbers.sort()

    if len(numbers) == 1:
        break

a = [950, 700]
# 210 + 250 + 290 + 330 + 370 + 410 + 540 + 700 + 950 + 1650

a.insert(0, 5); -> O(n)
# iterate and remove K chars and see if length changes ?
# what if removing letters decreases order?
# what if K is too long and multiple cases are in work?
# can removing letters increase length?

# How can we achieve the biggest compression?
# case 1   : merge two adjecent letter blocks (AAXAAYAAZ -> 6AXYZ)
# case 1.1 : merge two adjecent letter blocks that do no increase the order
#            of the count (i.e. 10s -> 100s  or 100s -> 1000s): "50KABC49K" -> "99K"
#            > saved_space = K + power_of_ten(highest_power_to_be_removed?) + 1
#            --------------------------------------------------------
# case 1.2 : merge two adjecent letter block that increase the order of the count
#            e.g. "50KABC50K" -> "100K"
#            > saved_space = K + length_of_highest_order
#            --------------------------------------------------------
# case 2   : remove individual letters that amount to K length, e.g. "ABC" or "A2B"
#            > saved_space = K
#            --------------------------------------------------------
# case 3   : remove letters of a continuous block
# case 3.1 : remove letters that decrease order of magnitude,
#            e.g. for K = 3: "100K" -> "97K", for K = 91: "100K" -> "9K"
#            > saved_space = order_of_magnitude(original_block)

def parse_chars(s: str) -> List[List[int, str]]:
    parsed_chars: List[List[int, str]] = [[1, s[0]]]

    for c in s[1:]:
        if c == parsed_chars[-1][1]:
            parsed_chars[-1][0] += 1
        else:
            parsed_chars.append([1, c])

    return parsed_chars


def stringify_block(block: List[int, str]) -> str:
    count, char = block

    if count > 1:
        return str(count) + char
    else:
        return char


def stringify_parsed(parsed_chars: List[List[int, str]]) -> str:
    return ''.join([stringify_block(block) for block in parsed_chars])


def solution_with_cases(s: str, k: int) -> int:
    parsed_chars: List[List[int, str]] = [[1, s[0]]]
    char_count: Dict[str, int] = {s[0]: 1}

    for c in s[1:]:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

        if c == parsed_chars[-1][1]:
            parsed_chars[-1][0] += 1
        else:
            parsed_chars.append([1, c])

    for char_block in parsed_chars:
        count, char = char_block

        if count < char_count[char]:
            # there are more blocks with the same char
            pass

    shortest_possible_compressed_length = len(s)

    return shortest_possible_compressed_length


def solution_with_smart_iteration(s: str, k: int):
    pass


tests = [
    ('ABBBCCDDCCC', 3, 5),
    ('AAAAAAAAAAABXXAAAAAAAAAA', 3, 3),
    ('ABCDDDEFG', 2, 6),
    ('KKKKKABCKKKKKXYZKKKK', 3, 7),  # 5KABC9K  10KXYZ4K
]


def run_tests(test_cases):
    for test in test_cases:
        s, k, answer = test
        assert answer == solution_with_cases(s, k)


run_tests(tests)
