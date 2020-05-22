def reverse(s):
    mid = len(s) // 2

    for i in range(mid):
        s[i], s[-(i+1)] = s[-(i+1)], s[i]

    return s


print(reverse(list("abcde")))
print(reverse(list("abcdef")))
