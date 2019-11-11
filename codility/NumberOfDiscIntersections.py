def solution(A):
    counter = 0
    N = len(A)
    stop_intersecting = [0] * N

    for i, r in enumerate(A):
        if i - r < 0:
            # we know the centers of the circles are incremental (0, 1, 2, 3, 4)
            # so if the radius of a circle "reaches" beyond 0 then it intersects all circles before it
            # or in other words we increment the counter with the number of circles before current
            # (i.e. the current index)
            counter += i
        else:
            # else the current circle reaches to the left to position (i - r)
            # and the current circle will intersect all previous circles
            # minus the number of circles that do not reach that far to the right (i.e. stop_intersecting[i - r])
            counter += i - stop_intersecting[i - r]  #

        if counter > 10000000:
            return -1

        stop_intersecting_at = i + r + 1

        if stop_intersecting_at < N:
            stop_intersecting[stop_intersecting_at] += 1

        if i + 1 < N:
            # we need the total of circles that cannot reach so far to the right
            stop_intersecting[i + 1] += stop_intersecting[i]
    return counter


print('[1, 5, 2, 1, 4, 0]', solution([1, 5, 2, 1, 4, 0]))
# print('[0, 0, 0, 0, 0, 0]', solution([0, 0, 0, 0, 0, 0]))
# print('[1, 1, 1, 0, 0, 1]', solution([1, 1, 1, 0, 0, 1]))




















