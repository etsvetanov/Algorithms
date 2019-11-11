# ()(()()(((()())(()()))
# ((

BRACKETS_MATCH = {
    '}': '{',
    ')': '(',
    ']': '['
}


def solution(S):
    stack = []

    if len(S) == 0:
        return 1

    for c in S:
        if c in '{([':
            stack.append(c)
        elif c in '])}':
            if not stack or stack.pop() != BRACKETS_MATCH[c]:
                return 0
        else:
            return 0

    if len(stack):
        return 0

    return 1
