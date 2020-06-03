from collections import defaultdict
from typing import Dict, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def DFS(node, row, column):
            if node is not None:
                nonlocal min_column, max_column
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        DFS(root, 0, 0)

        # order by column and sort by row
        ret = []
        for col in range(min_column, max_column + 1):
            columnTable[col].sort(key=lambda x: x[0])
            colVals = [val for row, val in columnTable[col]]
            ret.append(colVals)

        return ret


# Time O(w.h.logh)
# space O(n)


zero = TreeNode(0)
one = TreeNode(1)
three = TreeNode(3)
four = TreeNode(4)
seven = TreeNode(7)
eight = TreeNode(8)
nine = TreeNode(9)

three.left = nine
three.right = eight
nine.left = four
nine.right = zero
eight.left = one
eight.right = seven

root_node = three
solution = Solution()
print('result:')
print(solution.verticalOrder(root_node))
