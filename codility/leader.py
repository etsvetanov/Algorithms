def goldenLeader(A):
    n = len(A)
    size = 0
    value = None

    for x in A:
        if size == 0:
            size += 1
            value = x
        elif value != x:
            size -= 1
        else:
            size += 1

    leader = -1

    if size > 0:
        candidate = value
        count = 0

        for x in A:
            if x == candidate:
                count += 1

        if count > n // 2:
            leader = candidate

    return leader