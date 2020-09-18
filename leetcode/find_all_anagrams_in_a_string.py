from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        char_count = Counter(p)
        last_possible_idx = len(s) - len(p) + 1
        answers = []
        char_count_slice = Counter(s[:len(p)])


        for i in range(last_possible_idx):
            print(char_count_slice)
            if char_count_slice == char_count:
                answers.append(i)

            old = s[i]
            if not (i + len(p) < len(s)):
                break

            new = s[i + len(p)]



            char_count_slice[old] -= 1
            if char_count_slice[old] == 0:
                del char_count_slice[old]
            char_count_slice[new] += 1

        return answers


s = Solution()
print(s.findAnagrams("abab", "ab"))