class Node:  # Define the Node class
    def __init__(self,value,pointer):
        self.value = value  # The data field
        self.pointer = pointer  # The pointer field

    def get_next(self):    
        return self.pointer

class LinkedList:  # Define a linked list class
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_element(self,value):  # Add element at the first of the singly linked list
        new_node = Node(value,None)  # Create a new node
        new_node.pointer = self.head
        self.head = new_node
        self.size += 1
        
        if self.size == 1:  # If the original linked list is empty
            self.tail = new_node

def count_element(node_head):
    try:
        if node_head == None:  # If the current node is None, return 0
            return 0
        else:  # Otherwise, call the function recursively
            return 1 + count_element(node_head.get_next())
    except:
        print("Sorry, your input is invalid!")

def main():
    llist = LinkedList()
    llist.push_element(25)
    llist.push_element(5)
    llist.push_element(46)
    llist.push_element(7)
    llist.push_element(3.56)
    print("The length of the singly linked list is:",count_element(llist.head))
main()