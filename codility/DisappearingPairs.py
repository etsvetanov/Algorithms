# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from typing import Optional

CHARS = {'A', 'B', 'C'}

class Node:
    def __init__(self, c: str, left = None, right = None):
        self.c = c
        self.left = left
        self.right = right

def solution(S):
    # write your code in Python 3.6
    if S == "":
        return ""

    N = len(S)

    l = [Node(ch) for ch in S]

    for i, n in enumerate(l):
        if i > 0:
            n.left = l[i-1]
        if i < N - 1:
            n.right = l[i+1]

    head = l[0]
    curr = head

    while True:

        while curr and curr.right and curr.c == curr.right.c:
            if curr.left:
                curr.left.right = curr.right.right
            if curr.right.right:
                curr.right.right.left = curr.left

            new_curr = curr.left or curr.right.right

            if curr is head:
                head = new_curr

            curr = new_curr

        if not curr:
            break

        curr = curr.right


    # while True:
    #     has_pair = False
    #     curr = head
    #
    #     while curr:
    #         if not curr.right:  # if we are at the tail we don't have any work to do
    #             break
    #         if curr.c == curr.right.c:
    #             has_pair = True
    #
    #             # [ {curr.left} <-> {curr} <-> {curr.right} <-> {curr.right.right} ]
    #             # disappear curr and curr.right
    #             if curr.left:
    #                 curr.left.right = curr.right.right
    #
    #             if curr.right.right:
    #                 curr.right.right.left = curr.left
    #
    #             # adjust head
    #             if curr is head:
    #                 head = curr.right.right
    #
    #             curr = curr.right.right
    #         else:
    #             curr = curr.right
    #
    #     if not has_pair:
    #         break


    res = ''

    curr = head
    while curr:
        res += curr.c
        curr = curr.right

    return res



tests = [
    # "ABCDDCBA",
    "BABABA",
]

for test in tests:
    print(f'input: {test}, output: {solution(test)}')