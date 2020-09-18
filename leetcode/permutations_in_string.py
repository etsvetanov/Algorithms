from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        N = len(s1)
        s2_slice = Counter(s2[:N - 1])

        target = len(s1_count)
        current = sum(1 for k, v in s2_slice.items() if v == s1_count[k])

        for i in range(len(s2) - N + 1):
            new_char = s2[i + N - 1]
            s2_slice[new_char] += 1

            if s2_slice[new_char] == s1_count[new_char]:
                current += 1

            if target == current:
                return True

            old_char = s2[i]
            if s2_slice[old_char] == s1_count[new_char]:
                current -= 1

            s2_slice[old_char] -= 1

            # if s2_slice[old_char] == 0:
            #     del s2_slice[old_char]

        return False