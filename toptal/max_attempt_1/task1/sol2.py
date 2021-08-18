from functools import lru_cache
from typing import Optional, Tuple, Dict

Compr_Seg = Tuple[int, str]


class Segment:
    def __init__(
            self,
            start_idx: int,  # in original string, inclusive
            end_idx: int,  # in original string, inclusive
            compressed_form: Compr_Seg,
            left_acc_len: Optional[int] = None,  # length of compressed string from beginning to this segment, inclusive
            right_acc_len: Optional[int] = None,  # length of compressed string from end to this segment, inclusive

    ):
        self.start_idx = start_idx
        self.end_idx = end_idx
        self.left_acc_len = left_acc_len
        self.right_acc_len = right_acc_len
        self.compressed_form = compressed_form

    @staticmethod
    def get_len(seg: Compr_Seg):
        len_int = seg[0]

        return 1 if len_int == 0 else len(str(len_int)) + 1

    def __len__(self):
        return Segment.get_len(self.compressed_form)

    def get_new_length(self, delta):
        return Segment.get_len((self.compressed_form[0] + delta, self.compressed_form[1]))


class Solution:
    def get_min_compressed_len(self, s: str, k: int):
        seg_by_idx: Dict[int, Segment] = {}

        if len(s) == 0:
            return 0


        count = 0

        for i, c in enumerate(s):
            if i == len(s) - 1 or c != s[i+1]:
                start_idx = i - count
                end_idx = i

                seg = Segment(
                    start_idx=start_idx,
                    end_idx=end_idx,
                    compressed_form=(count+1, c)  # +1 to count curr char
                )

                for j in range(start_idx, end_idx+1):
                    seg_by_idx[j] = seg

                count = 0
            else:
                count += 1

        i = 0
        acc_len = 0

        while i < len(s):
            seg = seg_by_idx[i]
            acc_len = len(seg) + acc_len
            seg.left_acc_len = acc_len
            i = seg.end_idx + 1

        i = len(s) - 1
        acc_len = 0

        while i > - 1:
            seg = seg_by_idx[i]
            acc_len = len(seg) + acc_len

            seg.right_acc_len = acc_len
            i = seg.start_idx - 1


        min_len = seg_by_idx[0].right_acc_len

        for i, c in enumerate(s[:-(k+1)]):
            # removing [i:i+k]

            left_seg = None
            right_seg = None

            left_len = 0
            right_len = 0

            left_inner = i
            right_inner = i+k
            left_outer = i-1  # outer edge
            right_outer = i+k+1  # outer edge

            if i > 0:
                left_seg = seg_by_idx[left_outer]

            if right_outer < len(s):
                right_seg = seg_by_idx[right_outer]


            if left_seg and right_seg:
                if left_seg.compressed_form[1] == right_seg.compressed_form[1]:
                    # same char, we can merge
                    left_merge_len = left_inner - left_seg.start_idx
                    right_merge_len = right_seg.end_idx - right_inner

                    merged_seg_len = Segment.get_len((left_merge_len+right_merge_len, c))
                    total_length = merged_seg_len
                    if left_seg.start_idx > 0:
                        total_length += seg_by_idx[left_seg.start_idx-1].left_acc_len

                    if right_seg.end_idx < len(s) - 1:
                        total_length += seg_by_idx[right_seg.end_idx+1].right_acc_len

                    min_len = min(min_len, total_length)
                else:





                if left_seg is not seg_by_idx[i]:
                    # the removed K elements are at a segment boundary
                    left_len = left_seg.left_acc_len
                else:
                    left_len = left_seg.get_new_length(delta=left_seg.end_idx-left_outer)



                if right_seg is not seg_by_idx[right_inner]:
                    # the removed K elements are


        print('dsadas')


s = Solution()
res = s.get_min_compressed_len("ABBBCCDDCCC", 3)


# class Solution:
#     def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
#         # this decorator automatically use memo with key = (start, last, last_count, left)
#         @lru_cache(None)
#         def counter(start: int, prev_char: s, last_count, left):  # count the cost of compressing from the start
#             print(f'start {start} prev_char {prev_char} last_count {last_count} left {left}')
#             if left < 0:
#                 print('>>> inf')
#                 return float('inf')  # this is impossible
#             if start >= len(s):
#                 print('>>> 0')
#                 return 0
#             if s[start] == prev_char:
#                 # we have a stretch of the last_count of the same chars, what is the cost of adding one more?
#                 incr = 1 if last_count == 1 or last_count == 9 or last_count == 99 else 0
#                 # no need to delete here, if we have a stretch of chars like 'aaaaa' - we delete it from the beginning in the else delete section
#                 res = incr + counter(start + 1, prev_char, last_count + 1, left)
#                 print(f'>>> {res}')
#                 return res  # we keep this char for compression
#             else:
#                 # keep this char for compression - it will increase the result length by 1 plus the cost of compressing the rest of the string
#                 keep_counter = 1 + counter(start + 1, s[start], 1, left)
#                 # delete this char
#                 del_counter = counter(start + 1, prev_char, last_count, left - 1)
#                 res = min(keep_counter, del_counter)
#                 print(f'>>> ! {res}')
#                 return res
#
#         return counter(0, "", 0, k)
#
# s = Solution()
# res = s.getLengthOfOptimalCompression("ABBBCCDDCCC", 3)
#
# print(f'res: {res}')