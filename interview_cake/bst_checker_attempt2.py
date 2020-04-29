def is_binary_search_tree(root):
    # Determine if the tree is a valid binary search tree
    visited = [(root, root.value, root.value)]

    while len(visited):
        current, min_v, max_v = visited.pop()

        if min_v < current.left.value < current.value or current.value < current.right.value < max_v:
            return False

        visited.append((current.left, min(current.left.value, min_v), current.value))
        visited.append((current.right, current.value, max(max_v, current.right.value)))

    return True
