# What is a Queue?
# A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. It operates like a line where elements are added at one end (rear) and removed from the other end (front).
# Basic Operations of Queue Data Structure
# Enqueue (Insert): Adds an element to the rear of the queue.
# Dequeue (Delete): Removes and returns the element from the front of the queue.
# Peek: Returns the element at the front of the queue without removing it.
# Is_Empty: Checks if the queue is empty.
# Is_Full: Checks if the queue is full.
# -------------------------------------------------------------
# Example
# enqueue(2)/push(2):  # Pushes 2 at the end of the queue ([2])
# enqueue(1)/push(1):  # Pushes 1 at the end of the queue ([2,1])
# enqueue(3)/push(3):  # Pushes 3 at the end of the queue ([2,1,3])
# enqueue(4)/push(4):  # Pushes 4 at the end of the queue ([2,1,3,4])
# dequeue()/pop():     # Removes element at the start of the queue ([1,3,4]) i.e 2 which one entered first in the queue
# top()/peek():        # Returns first element in the queue i.e 1
# dequeue()/pop():     # Removes element at the start of the queue ([3,4]) i.e 1
# top()/peek():        # Returns first element in the queue i.e 3
# enqueue(7)/push(7):  # Pushes 4 at the end of the queue ([3,4,7])
# top()/peek():        # Returns first element in the queue i.e 3
# size():              # Returns 3 as total elements in the queue are 3.

# Implement a Queue using array.
class queue_impl:
    '''
    We are implementing the Queue Data Structure with Arrays
    The implementation with Array has some limitations so we are implementing Circular Queues.
    '''
    # Constructor
    def __init__(self, size) -> None:
        print("Creating a queue of length: ", size)
        self.queue = [None] * size
        self.size = size
        self.start = -1
        self.end = -1
        self.len = 0

    # Adding value to the queue
    def enqueue(self, val):
        if (self.end + 1)%self.size == self.start:
            print('Queue is full')
            return
        
        elif self.start == -1:
            self.start += 1
            self.end += 1
            self.len += 1
            self.queue[self.end] = val
        else:
            self.end = (self.end + 1) % self.size
            self.len += 1
            self.queue[self.end] = val
        print(f'Entered {val} in the queue at index {self.end}')

    # Return first value entered in the queue
    def dequeue(self):
        print('In DEQUEUE', self.start, self.end, self.len)
        if self.start == -1:
            print("Queue is Empty")
        elif self.len == 1 or self.start == self.end:
            temp = self.queue[self.start]
            self.end = -1
            self.start = -1
            self.len -= 1
            return temp
        else:
            temp = self.queue[self.start]
            self.start = (self.start + 1)%self.size
            self.len -= 1
            return temp

    # Returning the top element
    def peek(self):
        return self.queue[self.start] if self.start != -1 else "Queue is empty"
    
    # Returning the top element
    def peek_rear(self):
        return self.queue[self.end] if self.end != -1 else "Queue is empty"
    
    # Get length of queue
    def length(self):
        return self.len

    # Print queue
    def print(self):
        print(self.queue)
    
    # Check if queue is full or it has some space available
    def is_full(self):
        if self.len == self.size:
            return "Queue is Full"
        else:
            return "Queue has space available"

    # Print if queue is empty or it has some elements available
    def is_empty(self):
        if self.len == 0:
            return "Queue is Empty"
        else:
            return "Queue has some data available"

queue = queue_impl(4)
print('Is Queue Empty: ', queue.is_empty())
print('Is Queue Full: ', queue.is_full())
queue.dequeue()
print('Queue top element: ', queue.peek())
queue.enqueue(10)
queue.print()
print('Queue top element: ', queue.peek())
queue.enqueue(20)
queue.print()
print('Queue rear element: ', queue.peek_rear())
queue.enqueue(30)
queue.print()
queue.enqueue(40)
queue.print()
queue.enqueue(50)
queue.print()
# ---------------------------------------------------------------------------
print('Popped Element', queue.dequeue())
queue.print()
queue.enqueue(50)
queue.print()
print('Is Queue Full: ', queue.is_full())
queue.enqueue(60)
queue.print()
print('Popped Element', queue.dequeue())
print('Length of Queue', queue.length(), sep=' ')
queue.print()
print('Popped Element', queue.dequeue())
print('Length of Queue', queue.length(), sep=' ')
queue.print()
print('Popped Element', queue.dequeue())
print('Length of Queue', queue.length(), sep=' ')
queue.print()
print('Popped Element', queue.dequeue())
print('Length of Queue', queue.length(), sep=' ')
queue.print()
print('Popped Element', queue.dequeue())
queue.print()
queue.print()
print(queue.start, queue.end)
queue.enqueue(100)
queue.print()
print(queue.start, queue.end)