# 1. Define a class Node to describe a node of a doubly linked list.

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

""" 2. Define a class DLL to implement Doubly Linked List with _init_() method to create
 and initialise start reference variable. """

class DLLIterrator:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
class DLL:
    def __init__(self):
        self.start = None

# 3. Define a method is _empty) to check if the linked list is empty in DLL class.
    def is_empty(self):
        return self.start == None

# 4. In class DLL, define a method insert _at _start() to insert an element at the starting of
# the list. 
    def insert_at_start(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.start = new_node
            return
        current = self.start
        new_node.next = current
        current.prev = new_node
        self.start = new_node

# 5. In class DLL, define a method insert_at_last() to insert an element at the end of the

    def insert_at_last(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.start = new_node
            return
        current = self.start
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current

# 6. In class DLL, define a method search) to find the node with specified element value.
    def search(self, item):
        current = self.start
        while current is not None:
            if current.item == item:
                # print(f'Found {current.item}: before  {current.next.item} {current.next}')
                return current
            current = current.next
        print("Not found")
        return False

#  7. In class DLL, define a method insert _after) to insert a new node after a given node
# of the list. 

    def insert_after(self, after, item):
        search_node = self.search(after)
        if search_node:
            new_node = Node(item)
            new_node.next = search_node.next
            new_node.prev = search_node
            search_node.next = new_node
        else:
            print(f"Node with item {after} not found. Cannot insert after.")
            return False


# 8. In class DLL, define a method to print all the elements of the list.
    def display(self):
        current = self.start
        dll_list = []
        while current is not None:
            # print("ITEM", current.prev, current.item, current.next)
            dll_list.append(current.item)
            current = current.next
        print(dll_list)


# 9. In class DLL, implement iterator for DLL to access all the elements of the list in a
# sequence.
    # def __iter__(self):
    #     current = self.start
    #     while current is not None:
    #         yield current.item
    #         current = current.next
    #     return

    def __iter__(self):
        return DLLIterrator(self.start)

# 10. In class DLL, define a method delete first() to delete first element from the list.
    # def delete_first(self):
    #     if self.is_empty():
    #         print("List is empty")
    #         return
    #     current = self.start
    #     self.start = current.next
    #     current.next.prev = None
    #     current.next = None
    #     return

    def delete_first(self):
        current = self.start
        if current:
            self.start = current.next
            current.next = None
            return "DELETED"
        print("Empty List")
        return False
    
            

# 11. In class DLL, define a method delete_lastil) to delete last element from the list.
    def delete_last(self):
        if self.is_empty():
            print("List is empty")
            return
        current = self.start
        while current.next is not None:
            current = current.next
        current.prev.next = None
        current.prev = None
        return
# 12. In class DLL, define a method delete_item() to delete specified element from the list.

    # def delete_item(self, item):
    #     search_item = self.search(item)
    #     if search_item:
    #         if search_item.prev is None:
    #             # Deleting the first node
    #             self.start = search_item.next
    #         else:
    #             # Deleting a node in the middle
    #             search_item.prev.next = search_item.next
    #             search_item.next.prev = search_item.prev

    #         # Cleanup references of the deleted node
    #         search_item.next = None
    #         search_item.prev = None
    #         return True

    #     print(f'Not Found, Cannot delete {item}')
    #     return False

    def delete_item(self, item):
        search_item = self.search(item)
        if search_item:
            if search_item.prev == None:
                self.start = search_item.next
                search_item.next = None
                return True
            elif search_item.next == None:
                search_item.prev.next = None
                search_item.prev = None
                return True
            else:
                search_item.prev.next = search_item.next
                search_item.next.prev = search_item.prev
                search_item.prev = None
                search_item.next = None
                return
        print(f'Not Found, Cannot delete {item}')
        return False

dll = DLL()
print(dll.is_empty())
dll.insert_at_start(54)
dll.insert_at_start(67)
dll.insert_at_start(76)
dll.insert_at_last(455)
dll.insert_at_last(888)
print(dll.is_empty())
dll.display()
# dll.search(455)
dll.insert_after(455, 75)
dll.insert_after(76666, 00)
# dll.delete_first()
# dll.display()
# dll.delete_last()
# dll.display()
dll.delete_item(54)
dll.delete_item(6777)
dll.delete_item(888)
dll.display()

for i in dll:
    print(i)

# iterator = iter(dll)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))