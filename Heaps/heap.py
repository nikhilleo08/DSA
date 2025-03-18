import math
class MinHeap():
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap = []
    
    def heapify(self, heap):
        pass

    def push(self, val):
        if len(self.heap) == self.capacity:
            print('Cannot insert into heap as heap is already full, capacity:', len(self.heap))
            min_heap.printHeap()
            return
        self.heap.append(val)
        idx = len(self.heap) - 1
        while idx > 0 and self.heap[(idx-1)//2] > self.heap[idx]:
            self.heap[idx], self.heap[(idx-1)//2] = self.heap[(idx-1)//2], self.heap[idx]
            idx = (idx-1)//2
        print(f'{self.heap[idx]} is inserted into the heap')
    
    def printHeap(self):
        print('Heap:', self.heap)

min_heap = MinHeap(10)
min_heap.push(10)
min_heap.push(4)
min_heap.push(5)
min_heap.push(56)
min_heap.push(-1)
min_heap.printHeap()
min_heap.push(-10)
min_heap.push(100)
min_heap.push(485)
min_heap.push(-4)
min_heap.push(-2)
min_heap.push(-20)
min_heap.printHeap()