class Queue: # Queue class
    def __init__(self):
        self.items = []
    
    def enqueue(self, item): # Method to add elements to the queue
        self.items.append(item)
    
    def dequeue(self): # Method to remove elements from the queue
        if not self.is_empty(): # Check if the queue is not empty
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")
    
    def is_empty(self): # Method to check if the queue is empty
        return len(self.items) == 0

    def size(self): # Method to get the size of the queue
        return len(self.items)

    def peek(self): # Method to get the front element of the queue
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from empty queue")

queue = Queue() # Create a queue object
queue.enqueue(1) # Add element to the queue
queue.enqueue(2) # Add element to the queue
queue.enqueue(3) # Add element to the queue

print("Queue size:", queue.size())  # Output: Queue size: 3
print("Front element:", queue.peek())  # Output: Front element: 1

print("Dequeued element:", queue.dequeue())  # Output: Dequeued element: 1
print("Queue size after dequeue:", queue.size())  # Output: Queue size after dequeue: 2
