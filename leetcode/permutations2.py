from typing import List


class Solution:
    def permuteUnique(self, nums):
        print('nums:', nums)
        ans = [[]]
        for n in nums:
            print('ans:', ans)
            print('n:', n)
            new_ans = []
            for l in ans:
                print('l:', l, '(for l in ans)')
                # i represents the position we are going to 'plug' the new number in l
                # that's why it's len(l) + 1
                for i in range(len(l) + 1):
                    print('i', i, '(for i in range(len(l) + 1)')
                    new_ans.append(l[:i] + [n] + l[i:])
                    print('new_ans:', new_ans)
                    if i < len(l) and l[i] == n:
                        # if the number we are trying to plug 'n' same as ith number
                        # also it can't be same ith number if i==len(l) because it represents 'after the end'
                        print('skip')
                        break  # handles duplication
            ans = new_ans
            print('--------------------------------------------')

        return ans


solution = Solution()
result = solution.permuteUnique([2, 2, 1, 1])
print(result)

expected = [[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]]
assert result == expected
