from typing import List, Dict


# How can we achieve the biggest compression?
# case 1   : merge two adjecent letter blocks (AAAXYZAAA -> 6A)
# case 1.1 : multiple blocks that might have different impact (50K ABC 50K XYZ 49K -> 50K ABC 99K)
# case 2   :


def solution(s: str, k: int) -> int:
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


tests = [
    ('ABBBCCDDCCC', 3, 5),
    ('AAAAAAAAAAABXXAAAAAAAAAA', 3, 3),
    ('ABCDDDEFG', 2, 6),
    ('KKKKKABCKKKKKXYZKKKK', 3, 7),  # 5KABC9K
]


def run_tests(test_cases):
    for test in test_cases:
        s, k, answer = test
        assert answer == solution(s, k)


run_tests(tests)
