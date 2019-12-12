def solution(arr: []):
    start = arr[-1]
    curr = start

    for _ in range(len(arr)):
        print('going to the loo')
        curr = arr[curr]

    number_in_loop = curr
    loop_len = 1

    while arr[curr] != number_in_loop:
        curr = arr[curr]
        loop_len += 1

    curr1 = start
    curr2 = start

    for _ in range(loop_len):
        # advabce curr1 loop_len steps
        print('curr1:', curr1)
        curr1 = arr[curr1]

    print('loop_length:', loop_len)

    while curr1 != curr2:
        curr2 = arr[curr2]
        curr1 = arr[curr1]

    return curr1


#               0  1  2  3  4  5
# print(solution([3, 0, 4, 0, 1, 2]))
print(solution([2, 0, 1, 0, 4, 3]))