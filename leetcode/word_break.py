class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        memo = List[bool]

        def recurse(self, s: str, word_dict: set, start: int):
            if start == len(s):
                return True

            for end in range(start+1, len(s)+1):
                if s[start:end] in word_dict and recurse(end)

        return recurse(start=0)
