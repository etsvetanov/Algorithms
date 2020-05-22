class BinaryTreeNode:

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


#           start
#     left            right
# left   right    left   right

# left < start && right > start && left.left < left && left.right > left && right.left < right && right.right > right

#      40
#   30      50
# 20   35 45  55


A = BinaryTreeNode(40)
A.insert_left(30)
A.insert_right(50)
A.left.insert_left(20)
A.left.insert_right(50)
A.right.insert_left(45)
A.right.insert_right(50)


# THIS IS WRONG
def is_binary_search_tree(root):
    # Determine if the tree is a valid binary search tree

    visited = [(root, None, None)]  # (node, min, max)

    while visited:
        current, minn, maxx = visited.pop()
        value, left, right = current.value, current.left, current.right

        if current.right:
            if minn and right.value < minn or maxx and right.value > maxx:
                return False

            visited.append((right, value, maxx))

        if current.left:
            if minn and left.value < minn or maxx and left.value > maxx:
                return False

            visited.append((left, minn, value))

    return True


print(check_bst(A))
