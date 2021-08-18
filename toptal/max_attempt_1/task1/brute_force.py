def find_min_compr_len(s: str, k: int):
    def compute_compressed_len(s: str):
        total_l = 0
        count = 0

        for i, c in enumerate(s):

            if i == len(s) - 1 or c != s[i+1]:
                l = 1 if count == 0 else len(str(count+1))+1  # 1 if a single letter, count + 1 to account for curr
                total_l += l

                count = 0
            else:
                count += 1

        return total_l

    min_l = len(s)

    for i in range(len(s) - k - 1):
        new_l = compute_compressed_len(s[:i] + s[i+k:])
        print(f'i: {i}, new_s: {s[:i] + s[i+k:]} new_l: {new_l}, min_l: {min_l}')

        min_l = min(min_l, new_l)

    return min_l


tests = [
    ['ABBBCCDDCCC', 3, 5],
    [11*'A' + "BXX" + 10*'A', 3, 3],
    ['ABCDDDDEFG', 2, 6]
]


for test in tests:
    print(f'runing test {test}')
    res = find_min_compr_len(test[0], test[1])
    print(f'> {res}')
    assert res == test[2]


