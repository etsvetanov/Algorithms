# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.leaf_paths = []

    def dfs(self, node, path):
        current_path = path + [node.val]
        if not node.left and not node.right:
            self.leaf_paths.append(current_path)
        else:
            if node.left:
                self.dfs(node.left, current_path)
            if node.right:
                self.dfs(node.right, current_path)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return None

        self.dfs(root, [])
        return map(lambda path: '->'.join(map(str, path)), self.leaf_paths)
