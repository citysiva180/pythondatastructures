# Double linked list has 3 details
# -data
# previous
# Next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doubly_linkedlist:

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def delete(self, key):
        current_node = self.head
        while current_node != None:
            # Case 1
            if current_node.data == key and current_node == self.head:
                if not current_node.next:
                    current_node = None
                    self.head = None
                    return
                # Case 2
                else:
                    nxt = current_node.next
                    current_node.next = None
                    nxt.prev = None
                    current_node = None
                    self.head = nxt
                    return

            elif current_node.data == key:

                # Case 3
                if current_node.next:
                    nxt = current_node.next
                    prev = current_node.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current_node.next = None
                    current_node = None
                    current_node = None
                    return
                # Case 4
                else:
                    prev = current_node.prev
                    prev.next = None
                    current_node.prev = None
                    current_node = None
                    return
            current_node = current_node.next


newList = doubly_linkedlist()
newList.prepend(3)
newList.append(1)
newList.append(2)
newList.append(3)
newList.append(4)
newList.prepend(5)
newList.display()
print("After deletion")
newList.delete(4)
newList.display()
