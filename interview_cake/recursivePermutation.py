
def permutations(s):
    if len(s) == 2:
        return s, s[1] + s[0]

    my_set = []

    for i in range(len(s)):
        for s_perm in permutations(s[:i] + s[i + 1:]):
            my_set.append(s[i] + s_perm)

    return my_set

# { 'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}

answer = permutations('aabc')

print('permutations:', len(answer), ':', answer)