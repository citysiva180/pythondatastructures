# Simply to store data

class node:

    # Constructor
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class binary_search_tree:
    def __init__(self):
        self.root = None

    # Insert Elements in Binary Search Tree
    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)  # Private insert function

    # Inserting into the node, if there is no value in the left node
    # Then you would need to assign that value in that node.
    # More than this, you also need to check if the value entering is higher or lower
    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child == None:
                current_node.left_child = node(value)
            else:
                self._insert(value, current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child = node(value)
            else:
                self._insert(value, current_node.right_child)
        else:
            print("Value already in Tree")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node != None:
            self._print_tree(current_node.left_child)
            print(str(current_node.value))
            self._print_tree(current_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node == None:
            return current_height
        left_height = self._height(current_node.left_child, current_height+1)
        right_height = self._height(current_node.right_child, current_height+1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child != None:
            return self._search(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child != None:
            return self._search(value, current_node.right_child)
        return False


tree = binary_search_tree()

tree.insert(0)
tree.insert(12)
tree.insert(13)
tree.insert(22)
tree.insert(33)
tree.insert(54)
tree.insert(53)
tree.insert(52)
tree.insert(51)


tree.print_tree()
print("tree height : "+str(tree.height()))
print(tree.search(10))
print(tree.search(54))
