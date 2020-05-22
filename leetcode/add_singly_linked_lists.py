# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2

        head = ListNode(None, None)
        cur = head
        prev = None

        magn = 0
        carry = 0

        while cur1 or cur2:
            val = None
            summ = carry

            if cur1:
                summ += cur1.val
                cur1 = cur1.next

            if cur2:
                summ += cur2.val
                cur2 = cur2.next

            carry, val = summ // 10, summ % 10
            magn += 1

            cur.val = val
            prev = cur

            if (cur1 or cur2 or carry):
                cur = ListNode(None, None)
                prev.next = cur

        return head

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         n = 0

#         for l in (l1, l1):
#             cur = l
#             magn = 0

#             while cur:
#                 n += cur.val * 10 ** magn
#                 magn += 1
#                 cur = cur.next

#         return n