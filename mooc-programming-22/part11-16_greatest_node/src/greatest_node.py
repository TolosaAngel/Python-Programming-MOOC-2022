class Node:
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    max_node = root.value

    if root.left_child is not None:
        left_node = greatest_node(root.left_child)
    else:
        left_node = 0

    if root.right_child is not None:
        right_node = greatest_node(root.right_child)
    else:
        right_node = 0
    
    return max(max_node,right_node,left_node)

if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))