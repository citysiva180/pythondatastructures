#===========================#
# Sinlgy linked List python #
#===========================#

# Implement the node

# This is class node. It contains a data params and a next param.
# THe data param has the value which user passes
# The next param has the none value until it gets the next value

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# A Wrapper Class which will wrap all the node
# A head node gets an instance of node


# This is the linked list class. Which is our custom datastructure
# You are having a intializing constructure which accepts self as a param.
# There, we have a variable called the head, which is nothing but an instance of the node class

class linked_list:
    def __init__(self):
        self.head = node()

# The first thing that we might do is to add a value which is what the append function is for
# User is passing the data which a new node is created with the instance of the node function with data passed
# There is a current variable which is set to self.head, which again is a chaining of the node instance class.

# A condition checks if there is already value in the function.
# If there is a value, then we understand, that the value we plan to add should be the next value
# If there is no value in the data structure, then current value = new_node

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

# Finding length seems to be more easily. You are just using a counter to count the nodes

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next

        return total

# In all these cases, you just have to understand what the current node.next is doing.
# Cause that sems to get all the data needed.
# This is just a custom display function

    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)

        print(elements)


# Now, you could start adding functions to your data structure automatically
# Adding the get function

    def get(self, index):
        if index >= self.length():
            print("ERROR :  'Get' Index out of Range! ")
            return None

        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print("Error 'Erase' Index out of range! ")
            return None

        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1


my_list = linked_list()
my_list.append(1)
my_list.append(10)
my_list.append(45)
my_list.append(18)
my_list.append(99)

my_list.display()

print(my_list.get(2))

my_list.erase(4)
my_list.display()