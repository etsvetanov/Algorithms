from typing import List
from collections import Counter


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        summ = 0
        subarray_sum_count = Counter()
        subarray_sum_count[0] = 1

        for n in nums:
            summ += n

            if summ - k in subarray_sum_count:
                count += subarray_sum_count[summ - k]

            subarray_sum_count[summ] += 1

        return count
