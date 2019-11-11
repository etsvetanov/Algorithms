from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None


root = Node('A')
n1 = Node('B')
n2 = Node('C')
n3 = Node('D')
n4 = Node('E')

root.left = n1
root.right = n2
n1.left = n3
n1.right = n4


def pre_order(r, nodes) -> List[Node]:
    nodes.append(r.data)

    if r and r.left:
        pre_order(r.left, nodes)
    if r and r.right:
        pre_order(r.right, nodes)

    return nodes


pre_order(root, [])
