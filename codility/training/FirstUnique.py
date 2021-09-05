def solution(A):
    # write your code in Python 3.6
    idx_by_num = {}
    found = set()

    for i, n in enumerate(A):
        if n not in found:
            idx_by_num[n] = i
            found.add(n)
        else:
            if n in idx_by_num:
                del idx_by_num[n]

    # print(f'idx_by_num: {idx_by_num}')
    if not idx_by_num: return -1

    n, i = min(idx_by_num.items(), key=lambda x: x[1])

    return n