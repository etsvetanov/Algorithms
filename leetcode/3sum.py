from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        solutions = set()
        d = {}

        for n in nums:  # O(n)
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1

        # x + y + z = 0
        # -x = y + z

        # [x, y, z, w, t]
        # x, [y, z, w, t] -> xy, xz, xw, xt
        # y, [z, w, t] -> yz, yw, yt
        # ...
        unique_numbers = list(d.keys())

        if 0 in unique_numbers and d[0] >= 3:
            solutions.add('0,0,0')

        # unique_numbers = [x, y, z, w, t]
        # d = {x: 1, y: 1, z: 1, w: 1, t: 1}
        # x, [y, z, w, t]
        # -(x + z) = x
        #

        while len(unique_numbers) >= 2:
            x, *rest = unique_numbers

            for y in rest:
                z = -(x + y)

                if z in d:  # O(1)
                    if z in (x, y):
                        if d[z] > 1:
                            srtd_str = ','.join(map(str, sorted([x, y, z])))
                            if srtd_str not in solutions:
                                solutions.add(srtd_str)
                    else:
                        srtd_str = ','.join(map(str, sorted([x, y, z])))
                        if srtd_str not in solutions:
                            solutions.add(srtd_str)

            unique_numbers = rest

        #             tmp_set = [-2, 4]
        #             x -> [y, z, w, t]
        #             ans = x(x + y)
        #             d[-2] > 1

        return [s.split(',') for s in solutions]