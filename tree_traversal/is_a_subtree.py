from typing import List, Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


# left tree
root = Node(10)
n1 = Node(4)
n2 = Node(6)
n3 = Node(30)

n1.right = n3
root.left = n1
root.right = n2

# right tree
root_r = Node(26)
n1_r = Node(10)
n2_r = Node(3)
n3_r = Node(4)
n4_r = Node(6)
n5_r = Node(3)
n6_r = Node(30)

n3_r.right = n6_r
n1_r.left = n3_r
n1_r.right = n4_r
n2_r.right = n5_r
root_r.left = n1_r
root_r.right = n2_r


# in-order traversal
def in_order(r: Node, nodes: List[int]) -> List[int]:
    if r and r.left:
        in_order(r.left, nodes)

    nodes.append(r.data)

    if r and r.right:
        in_order(r.right, nodes)

    return nodes


# pre-order traversal
def pre_order(r: Node, nodes: List[int]) -> List[int]:
    nodes.append(r.data)
    if r and r.left:
        pre_order(r.left, nodes)

    if r and r.right:
        pre_order(r.right, nodes)

    return nodes


# function that takes two root nodes and determines if
# the first tree is a subtree of the second tree
def is_subtree(root_a: Node, root_b: Node) -> bool:
    inord1 = '-'.join(map(lambda i: str(i), in_order(root_a, [])))  # 4-30-10-6
    inord2 = '-'.join(map(lambda i: str(i), in_order(root_b, [])))  # 4-30-10-6-26-3-3
    preord1 = '-'.join(map(lambda i: str(i), pre_order(root_a, [])))  # 10-4-30-6
    preord2 = '-'.join(map(lambda i: str(i), pre_order(root_b, [])))  # 26-10-4-30-6-3-3

    return inord1 in inord2 and preord1 in preord2


is_subtree(root, root_r)
