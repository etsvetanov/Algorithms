class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0

        def recurse(i: int, prev: str = None):
            if i == len(s):
                if not prev:
                    nonlocal count
                    count += 1
                return

            char = s[i]

            if prev:
                if prev == '2' and int(char) > 6:
                    return  # not a valid decode
                recurse(i + 1)
            else:
                if char == '1' or char == '2':
                    recurse(i + 1, char)

                if char == '0':  # not a valid decode
                    return

                recurse(i + 1)

        recurse(0, False)

        return count

s = Solution()
ans = s.numDecodings('9272971672512277354953939427689518239714228293463398742522722274929422229859968434281231132695842184')
print('answer:', ans)