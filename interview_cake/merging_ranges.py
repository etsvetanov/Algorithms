def merge_ranges(ranges):
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    # O(nlogn)

    merged = [sorted_ranges[0]]

    # O(n)
    for r in sorted_ranges[1:]:
        curr_start, curr_end = merged[-1]
        next_start, next_end = r

        if next_start <= curr_end:
            merged[-1] = (curr_start, next_end)
        else:
            merged.append(r)

    return merged


test1 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# print (merge_ranges(test1))

assert merge_ranges(test1) == [(0, 1), (3, 8), (9, 12)]
