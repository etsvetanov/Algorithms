from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memo_checked = [False] * len(s)

        def recurse(start) -> bool:
            for end in range(start + 1, len(s)+1):
                if s[start:end] in word_set:
                    if end == len(s):
                        return True

                    if not memo_checked[end] and recurse(end):
                        return True
                    else:
                        memo_checked[end] = True

            return False

        return recurse(0)


s = Solution()
ans = s.wordBreak('leetcode', ['leet', 'code'])

print('ans:', ans)

# from typing import List
#
#
# # noinspection PyPep8Naming
# class Solution:
#     @staticmethod
#     def wordBreak(s: str, wordDict: List[str]) -> bool:
#         word_dict = set(wordDict)
#         memo = List[bool]
#
#         def recurse(start: int) -> bool:
#             print('start:', start)
#             if start == len(s):
#                 return True
#
#             print(f'[{start}...{len(s) + 1}]')
#             for end in range(start+1, len(s)+1):
#                 print('end:', end, 'start:', start)
#                 if s[start:end] in word_dict and recurse(end):
#                     print('FOUND IT')
#                     return True
#
#             return False
#
#         return recurse(start=0)
#
#
# # Solution.wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"])
# Solution.wordBreak('aaaaaaaaaaa', ['bbbb', 'bb', 'b', 'bbbbbb'])