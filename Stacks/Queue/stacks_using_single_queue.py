# # What is a Stack?
# # A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. It behaves like a stack of plates, where the last plate added is the first one to be removed.
# # Basic Operations of Stack Data Structure
# # -------------------------------------------------------------
# # push(): Add a value into the stack
# # pop(): Remove the top most element from the stack
# # top(): Get the top most element from the stack without removing it.
# # size(): Get the number of elements present in the stack.
# # IsEmpty: Check if the stack is empty
# # IsFull: Check if the stack is full
# # -------------------------------------------------------------
# # Example:
# # push(2) # Pushes 2 at the end of the stack ([2,])
# # push(3) # Pushes 3 at the end of the stack ([2,3])
# # push(4) # Pushes 4 at the end of the stack ([2,3,4])
# # push(1) # Pushes 1 at the end of the stack ([2,3,4,1])
# # top()   # Prints 1 as 1 was the Last element inserted into the stack.
# # pop()   # Returns 1 as 1 was the Last element inserted into the stack and also removes it from the stack. ([2,3,4])
# # push(5) # Pushes 5 at the end of the stack ([2,3,4,5])
# # top()   # Prints 5 as 5 was the Last element inserted into the stack.
# # pop()   # Returns 5 as 5 was the Last element inserted into the stack and also removes it from the stack. ([2,3,4])
# # pop()   # Returns 4 as 4 was the Last element inserted into the stack and also removes it from the stack. ([2,3])
# # pop()   # Returns 3 as 3 was the Last element inserted into the stack and also removes it from the stack. ([2])
# # push(9) # Pushes 9 at the end of the stack ([2,9])
# # top()   # Prints 9 as 9 was the last element inserted into the stack.
# # size()  # prints 2 as there are only 2 elements into the stack.
# # push(5) # Pushes 9 at the end of the stack ([2,9, 5])
# # size()  # prints 3 as there are only 3 elements into the stack.
# # -------------------------------------------------------------
# # -------------------------------------------------------------
from collections import deque

# Implement a stack using Two Queues.
# Queue1: Holds the elements that represent the stack.
# Queue2: A temporary queue used to help with the push() operation to reorder the elements.
class StackUsingQueue:
    # Constructor
    def __init__(self, size) -> None:
        self.queue1 = deque(maxlen=size)
        self.size = size
        self.length = 0

    # Adding value to the stack
    def push(self, val):
        print(f'Pusing {val} in stack')
        self.queue1.append(val)
        self.length += 1

        for i in range(self.length-1):
            self.queue1.append(self.queue1.popleft())

    # Returning the top element
    def top(self):
        if self.length != 0:
            return self.queue1[0]
        else:
            return self.is_empty()

    # Return last value entered in the stack
    def pop(self):
        # If the queue is empty, return None
        if not self.queue1:
            return None
        self.length -= 1
        return self.queue1.popleft()
    
    # Print  stack
    def print(self):
        for i in range(len(self.queue1)):
            print(self.queue1[i], end=' ' if i < len(self.queue1) - 1 else '')
    
    # Print  stack
    def is_full(self):
        if len(self.queue1) == self.size:
            return "Stack is full"
        else:
            return "Stack has space availabel"

    # Print  stack
    def is_empty(self):
        if len(self.queue1) == 0:
            return "Stack is empty"
        else:
            return "Stack has elements availabel"
        
stack = StackUsingQueue(4)
print('Is Stack Empty:', stack.is_empty())
stack.push(100)
stack.push(200)
stack.push(300)
stack.push(400)
print('Stack Top:', stack.top())
print('Is Stack Full:', stack.is_full())
print()
print('Current Stack state:')
stack.print()
print('\n')
print('Popped element:', stack.pop())
print('Stack Top:', stack.top())
print()
print('Current Stack state:')
stack.print()
print('\n')
print('Popped element:', stack.pop())
print('Popped element:', stack.pop())
print('Popped element:', stack.pop())
print('Stack Top:', stack.top())
print()
print('Current Stack state:')
stack.print()
print('\n')
print('Is Stack Empty:', stack.is_empty())
print('Current Stack state:')
stack.print()