from typing import List


def find_seat_solutions(input: List[str], curr: List[str] = [], results: List[List[str]] = []):
    print('input:', input, 'curr:', curr, 'results:', results)
    if not input:
        results.append(curr)
    else:
        for i in range(len(input)):
            if i == 1 and input[i].startswith('g'):
                continue
            find_seat_solutions(input=input[:i] + input[i+1:], curr=curr + [input[i]], results=results)

    return results

print(find_seat_solutions(input=['b1', 'b2', 'g1']))
