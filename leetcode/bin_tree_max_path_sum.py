from queue import

q = LifoQueue
q.put(5)
q.get()


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxx = float('-inf')

    def find_gain(self, node) -> int:
        left_gain = max(self.find_gain(node.left), 0) if node.left else 0
        right_gain = max(self.find_gain(node.right), 0) if node.right else 0

        gain = node.val + left_gain + right_gain

        self.maxx = max(self.maxx, gain)

        return node.val + max(left_gain, right_gain)

    def maxPathSum(self, root: TreeNode) -> int:
        self.find_gain(root)

        return self.maxx

