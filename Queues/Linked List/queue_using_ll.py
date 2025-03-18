class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class QueueUsingLinkedList:
    def __init__(self, size) -> None:
        print("Creating a queue of size", size)
        self.size = size
        self.len = 0
        self.start = None
        self.end = None
    
    # TC: O(1)
    def enqueue(self, val):
        if self.size == self.len:
            print("queue is full cannot add more elements")
            return
        else:
            if not self.start:
                curr = Node(val)
                curr.next = self.start
                self.start = curr
                self.end = curr
                self.len += 1
            else:
                curr = Node(val)
                self.end.next = curr
                self.end = curr
                self.len += 1
        print(f"Added {val} into the queue")

    # TC: O(1)
    def dequeue(self):
        if self.len == 0:
            print("queue is empty cannot dequeue")
        else:
            curr = self.start
            top_val = curr.val
            self.start = curr.next
            self.len -= 1
            del curr
            return top_val
    
    # TC: O(1)
    def start_element(self):
        if self.len == 0:
            print("queue is empty cannot get Start element")
            return 
        print("Start element of the queue:", self.start.val)
    
    # TC: O(1)
    def length(self):
        print("Length of queue:", self.len)
    
    # TC: O(1)
    def is_full(self):
        if self.len == self.size:
            print("queue is Full", self.len)
            return
        else:
            print(f"queue has {self.size -  self.len} space left")
    
    # TC: O(1)
    def is_empty(self):
        if self.len == 0:
            print("queue is Empty")
            return

    # TC: O(N)
    def print_queue(self):
        if not self.start:
            self.is_empty()
        curr = self.start
        while curr:
            print(curr.val, end=' ' if curr.next else '\n')
            curr = curr.next
        return

queue = QueueUsingLinkedList(4)
queue.start_element()
queue.enqueue(100)
queue.is_full()
queue.enqueue(200)
queue.enqueue(300)
queue.enqueue(400)
queue.is_full()
queue.enqueue(500)
queue.length()
queue.start_element()
print('Printing queue: ', end=' ')
queue.print_queue()
print('Before removal')
queue.print_queue()
queue.dequeue()
print('After removal')
queue.print_queue()
queue.length()
queue.start_element()
print('Before removal')
queue.print_queue()
queue.dequeue()
print('After removal')
queue.print_queue()
print('Before removal')
queue.print_queue()
queue.dequeue()
print('After removal')
queue.print_queue()
queue.length()
print('Before removal')
queue.print_queue()
queue.dequeue()
print('After removal')
queue.print_queue()
queue.length()