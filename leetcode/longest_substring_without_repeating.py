def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0

    if len(s) == 1:
        return 1

    longest_length = 0

    for i in range(len(s)):
        char_set = set()
        for c in s[i:]:
            if c in char_set:
                break
            else:
                char_set.add(c)
                longest_length = max(longest_length, len(char_set))


    return longest_length


print(lengthOfLongestSubstring("au"))
