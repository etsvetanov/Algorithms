from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        N = len(s1)
        s2_slice = Counter(s2[:N - 1])

        target = len(s1_count)
        current = sum(1 for k, v in s2_slice.items() if v == s1_count[k])
        print('target:', target)
        print('s1_count:', s1_count)

        for i in range(len(s2) - N + 1):
            print('s2_slice', s2_slice)
            print('current:', current)
            new_char = s2[i + N - 1]
            s2_slice[new_char] += 1


            if s2_slice[new_char] == s1_count[new_char]:
                current += 1  # we've reach exact number of characters
            elif s1_count[new_char] and s2_slice[new_char] == s1_count[new_char] + 1:
                current -= 1  # we've passed exact number of characters

            if target == current:
                return True

            old_char = s2[i]
            s2_slice[old_char] -= 1

            if s1_count[old_char] and s2_slice[old_char] + 1 == s1_count[old_char]:
                current -= 1
            elif s1_count[old_char] and s2_slice[old_char] == s1_count[old_char]:
                current += 1


            # if s2_slice[old_char] == 0:
            #     del s2_slice[old_char]

        return False


s = Solution()
ans = s.checkInclusion(s1="ab", s2="eidbaooo")
# ans = s.checkInclusion(s1='abc', s2='bbbca')
print('ans:', ans)
