# What is a Stack?
# A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. It behaves like a stack of plates, where the last plate added is the first one to be removed.
# Basic Operations of Stack Data Structure
# -------------------------------------------------------------
# push(): Add a value into the stack
# pop(): Remove the top most element from the stack
# top(): Get the top most element from the stack without removing it.
# size(): Get the number of elements present in the stack.
# IsEmpty: Check if the stack is empty
# IsFull: Check if the stack is full
# -------------------------------------------------------------
# Example:
# push(2) # Pushes 2 at the end of the stack ([2,])
# push(3) # Pushes 3 at the end of the stack ([2,3])
# push(4) # Pushes 4 at the end of the stack ([2,3,4])
# push(1) # Pushes 1 at the end of the stack ([2,3,4,1])
# top()   # Prints 1 as 1 was the Last element inserted into the stack.
# pop()   # Returns 1 as 1 was the Last element inserted into the stack and also removes it from the stack. ([2,3,4])
# push(5) # Pushes 5 at the end of the stack ([2,3,4,5])
# top()   # Prints 5 as 5 was the Last element inserted into the stack.
# pop()   # Returns 5 as 5 was the Last element inserted into the stack and also removes it from the stack. ([2,3,4])
# pop()   # Returns 4 as 4 was the Last element inserted into the stack and also removes it from the stack. ([2,3])
# pop()   # Returns 3 as 3 was the Last element inserted into the stack and also removes it from the stack. ([2])
# push(9) # Pushes 9 at the end of the stack ([2,9])
# top()   # Prints 9 as 9 was the last element inserted into the stack.
# size()  # prints 2 as there are only 2 elements into the stack.
# push(5) # Pushes 9 at the end of the stack ([2,9, 5])
# size()  # prints 3 as there are only 3 elements into the stack.
# -------------------------------------------------------------
# -------------------------------------------------------------

# Implement a stack using array.
class st_impl:
    # Constructor
    def __init__(self, size) -> None:
        self.top_idx = -1
        self.stack = []
        self.size = size
        print("Creating a stack with size", size)

    # Adding value to the stack
    def push(self, val):
        if len(self.stack) == self.size:
            print('Stack is full')
            return
        print(f'Inserting {val} in the stack')
        self.top_idx += 1
        self.stack.append(val)

    # Returning the top element
    def top(self):
        if self.top_idx >= 0 and self.stack:
            return self.stack[self.top_idx]
        else:
            return 'Stack is empty'

    # Return last value entered in the stack
    def pop(self):
        if self.stack:
            val = self.stack[self.top_idx]
            self.top_idx -= 1
            self.stack.pop()
            return val
        else:
            return 'Stack is empty'
    
    # Get length of stack
    def length(self):
        if self.stack:
            return self.top_idx + 1
        else:
            return 'Stack is empty'
    
    # Print  stack
    def print(self):
        print(self.stack)
    
    # Print  stack
    def is_full(self):
        if len(self.stack) == self.size:
            return 'Stack is full'
        else:
            return f'Stack has {self.size - self.length()} spaces available'
    
    # Print  stack
    def is_empty(self):
        if len(self.stack) == 0:
            return 'Stack is Empty'
        else:
            return f'Stack has {self.length()} elements available'
            
        
stack = st_impl(3)
print('Checking if stack is empty:', stack.is_empty())
stack.push(400)
stack.push(200)
print('Checking if the stack is Full: ', stack.is_full())
stack.push(100)
print('Checking if stack is empty:', stack.is_empty())
print('Checking if the stack is Full: ', stack.is_full())
stack.push(3)
print('Current Stack State', end=' ')
stack.print()
print('Stack Top:',stack.top())
print('Popping element from stack:',stack.pop())
print('Current Stack State', end=' ')
stack.print()
print("Stack Top", stack.top())
stack.print()
print("Popping element from stack: ",stack.pop())
print("Stack Top", stack.top())
stack.print()
print("Popping element from stack: ",stack.pop())
print("Stack Top", stack.top())
stack.print()
print("Popping element from stack: ",stack.pop())
stack.print()
print("Stack Top", stack.top())
stack.push(40)
stack.push(20)
stack.push(10)
stack.push(30)
print('Stack Length:', stack.length())
print('Stack Max Size:', stack.size)
print('Stack Top:', stack.top())
stack.print()
