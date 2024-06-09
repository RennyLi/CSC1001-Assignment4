# Define a node class
class Node():  
    def __init__(self, value=None):
        self.value = value  # The value field
        self.pointer = None  # The pointer field

# Define the linked queue class
class LinkedQueue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def first(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            return self.head.element

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            answer = self.head.element
            self.head = self.head.pointer
            self.size -= 1
            if self.is_empty():
                self.tail = None
            return answer
    
    def enqueue(self,e):
        newest = Node(e)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.pointer = newest
        self.tail = newest
        self.size += 1

    # Print all the items
    def print(self):
        print(self.head)

    # Get the value of the item according to the index
    def getItem(self, index):
        item = self.head
        count = 0
        if item != None:
            while count != index:
                item = item.pointer
                count += 1
            return item.value

    # Set the value of the item according to the index
    def setItem(self, index, value):
        item = self.head
        count = 0
        if item != None:
            while count < index:
                item = item.pointer
                count += 1
            item.value = value

    # Swap the values of the two items
    def swapItem(self, i, j):
        temp = self.getItem(j)
        self.setItem(j, self.getItem(i))
        self.setItem(i, temp)

    def quicksort(self, left, right):
        if left < right:
    		# Initialize the i and j values
            i = left
            j = i + 1
            start = self.getItem(i)

        	# The general condition is that j cannot be larger than the length of the linked queue
            while j <= right:
        		# If j value is larger or equal to the base start value, then skip it
                while j <= right and self.getItem(j) >= start:
                    j += 1
        	    # Otherwise, if j value is smaller than the base start value, then swap the i and j items
                if j <= right:
                    i += 1
                    self.swapItem(i, j)
                    j += 1
            self.swapItem(left, i)
            self.quicksort(left, i - 1)
            self.quicksort(i + 1, right)

def main():
    lq = LinkedQueue()
    lq.enqueue(5)
    lq.enqueue(8)
    lq.enqueue(10)
    lq.enqueue(11)
    lq.quicksort(0,3)
    lq.print()
main()