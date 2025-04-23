from heap import Heap

class MinHeap(Heap):
    """
    This class implements a MinHeap, which is a complete binary tree where the value of each node is less than or equal to the values of its children.
    It inherits from the Heap class.
    Ensures the smallest element is always at the top.
    """
    def __init__(self):
        """
        Initialize an empty MinHeap using a list.
        """
        super().__init__()
    
    def insert(self, value):
        """
        Inserts a value into the MinHeap and maintains the heap property.
        """
        self._heap.append(value)  # Add to the end
        self._heapify_up(self.size() - 1)  # Restore MinHeap property

    def _heapify_up(self, index):
        """
        Restores the MinHeap property by bubbling the element at `index` up.
        """
        while index > 0:
            parent_index = self._parent(index)
            if self._heap[index] < self._heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break
 
    def extract(self):
        pass
    

    def _heapify_down(self, index):
        pass

if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.insert(4)
    min_heap.insert(40)
    min_heap.insert(20)
    min_heap.insert(30)
    min_heap.insert(10)

    print(min_heap._heap)  # Output should be [10, 20, 30, 40]

#       4
#   10      20
# 40  30