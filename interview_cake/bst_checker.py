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
def check_bst(node: BinaryTreeNode):
    print('node.value:', node.value)
    if node.left:
        if node.right:
            # both present
            if node.left.value > node.value or node.right.value < node.value:
                return False

            return check_bst(node.left) and check_bst(node.right)
        else:
            # only left present
            if node.left.value > node.value:
                return False

            return check_bst(node.left)
    elif node.right:
        # only right is present
        if node.right.value < node.value:
            return False

        return check_bst(node.right)

    return True




print(check_bst(A))
