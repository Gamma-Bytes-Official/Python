# Implementation of the stack data structure in Python.
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item): # Push method to add elements to the stack
        self.items.append(item)
    
    def pop(self): # Pop method to remove elements from the stack
        if not self.is_empty(): # Check if the stack is not empty
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")
    
    def is_empty(self): # Method to check if the stack is empty
        return len(self.items) == 0

    def peek(self): # Method to get the top element of the stack
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self): # Method to get the size of the stack
        return len(self.items)

stack = Stack() # Creating a stack
stack.push(1) # Pushing elements to the stack
stack.push(2)  # Pushing elements to the stack
stack.push(3) # Pushing elements to the stack

print("Stack size:", stack.size())  # Output: Stack size: 3
print("Top element:", stack.peek())  # Output: Top element: 3

print("Popped element:", stack.pop())  # Output: Popped element: 3
print("Stack size after pop:", stack.size())  # Output: Stack size after pop: 2
