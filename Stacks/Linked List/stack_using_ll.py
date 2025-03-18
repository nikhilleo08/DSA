class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class StackUsingLinkedList:
    def __init__(self, size) -> None:
        print("Creating a stack of size", size)
        self.size = size
        self.len = 0
        self.top = None
    
    # TC: O(1)
    def push(self, val):
        if self.size == self.len:
            print("Stack is full cannot add more elements")
            return
        else:
            curr = Node(val)
            curr.next = self.top
            self.top = curr
            self.len += 1
        print(f"Added {val} into the stack")

    # TC: O(1)
    def pop(self):
        if self.len == 0:
            print("Stack is empty cannot pop")
        else:
            curr = self.top
            top_val = curr.val
            self.top = self.top.next
            self.len -= 1
            del curr
            return top_val
    
    # TC: O(1)
    def top_element(self):
        if self.len == 0:
            print("Stack is empty cannot get top element")
            return 
        print("Top element of the stack:", self.top.val)
    
    # TC: O(1)
    def length(self):
        print("Length of Stack:", self.len)
    
    # TC: O(1)
    def is_full(self):
        if self.len == self.size:
            print("Stack is Full", self.len)
            return
        else:
            print(f"Stack has {self.size -  self.len} space left")
    
    # TC: O(1)
    def is_empty(self):
        if self.len == 0:
            print("Stack is Empty")
            return

    # TC: O(N)
    def print_stack(self):
        if not self.top:
            self.is_empty()
        curr = self.top
        while curr:
            print(curr.val, end=' ' if curr.next else '\n')
            curr = curr.next
        return

stack = StackUsingLinkedList(4)
stack.top_element()
stack.push(100)
stack.push(200)
stack.push(300)
stack.push(400)
stack.is_full()
stack.push(500)
stack.length()
stack.top_element()
print('Printing Stack: ', end=' ')
stack.print_stack()
print('Before removal')
stack.print_stack()
stack.pop()
print('After removal')
stack.print_stack()
stack.length()
stack.top_element()
print('Before removal')
stack.print_stack()
stack.pop()
print('After removal')
stack.print_stack()
print('Before removal')
stack.print_stack()
stack.pop()
print('After removal')
stack.print_stack()
stack.length()
print('Before removal')
stack.print_stack()
stack.pop()
print('After removal')
stack.print_stack()
stack.length()