from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            print('first:', first, 'curr:', curr)
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
                print('output:', output, '----------------')
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                print('[{0}]curr:'.format(i), curr)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output


solution = Solution()
input = [1, 2, 3]
result = solution.subsets(input)
print('\nresult:', result)