import unittest


def is_balanced(tree_root):
    # Determine if the tree is superbalanced

    min_depth = None
    max_depth = 0

    # current = tree_root

    to_visit = [(tree_root, 0)]

    while len(to_visit) > 0:
        print(to_visit)
        current, depth = to_visit.pop()

        if current.left:
            to_visit.append((current.left, depth + 1))
        if current.right:
            to_visit.append((current.right, depth + 1))

        if not current.left and not current.right:
            min_depth = depth if not min_depth else min(depth, min_depth)
            max_depth = max(depth, max_depth)

    print('min:', min_depth, 'max:', max_depth)

    if abs(min_depth - max_depth) > 1:
        return False

    return True


class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def get_tree():
    tree = BinaryTreeNode(1)
    left = tree.insert_left(5)
    right = tree.insert_right(9)
    right_left = right.insert_left(8)
    right.insert_right(5)
    right_left.insert_left(7)

    return tree


print(is_balanced(get_tree()))
