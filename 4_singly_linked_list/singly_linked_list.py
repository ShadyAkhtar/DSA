# 1. Define a class Node to describe a node of a singly linked list.
# 2. Define a class SLL to implement Singly Linked List with
# and initialise start reference variable.
# _init_() method to create
# 3. Define a method is _empty) to check if the linked list is empty in SLL class.

# 4. In class SLL, define a method insert _at start() to insert an element at the starting of
# the list.

# 5. In class SLL, define a method insert _at _last() to insert an element at the end of the
# list.

# 6. In class SLL, define a method search) to find the node with specified element value.

# 7. In class SLL, define a method insert after() to insert a new node after a given node
# of the list.

class Node():
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class SLL():
    def __init__(self, start=None):
        new_node = Node(start)
        self.start = new_node

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, item):
        new_node = Node(item, self.start)
        self.start = new_node

    def insert_at_last(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.start = new_node
            return
        current = self.start
        while current.next is not None:
            current = current.next

        current.next = new_node

    def search(self, item):
        current = self.start
        while current is not None:
            if current.item == item:
                print(f'Found {current.item}: before  {current.next.item} {current.next}')
                return current
            current = current.next
        print("Not Found")
        return False

    def insert_after(self, item, after):
        search_node = self.search(after)
        if search_node:
            new_node = Node(item, search_node.next)
            search_node.next = new_node
        else:
            print(f"Node with item {after} not found. Cannot insert after.")

    def display(self):
        current = self.start
        sll_list = []
        while current is not None:
            sll_list.append(current.item)
            current = current.next
        print(sll_list)

# [25, 4, 78, 96, 32, 541, 25] 

sll = SLL(100)
print(f'SLL empty: {sll.is_empty()}')

sll.insert_at_start(4)
sll.insert_at_start(25)
sll.insert_at_last(78)
sll.insert_at_last(32)
sll.display()
sll.insert_after(96, 78)
sll.insert_at_last(25)
sll.insert_after(541, 32)
sll.search(541)
sll.search(5410)
sll.display()
            