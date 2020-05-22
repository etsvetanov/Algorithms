class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


# pass by reference value
def delete_node(node: LinkedListNode):
    node.value = node.next.value
    node.next = node.next.next


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(c)

pass
# a.next -> b
# b.next -> c
# c.next -> None
# a -> b -> None