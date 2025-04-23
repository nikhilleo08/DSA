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
        """
        Removes and returns the minimum element from the MinHeap.
        Maintains the MinHeap property after removal.
        """
        # Check if heap is empty
        if self.is_empty():
            raise IndexError("Cannot extract from an empty heap.")
        
        # Element to return
        min_value = self._heap[0]
        
        # Move the last element to the root and shrink the heap
        popped = self._heap.pop()
        if not self.is_empty():
            self._heap[0] = popped
            self._heapify_down(0)
        
        # Return the minimum value from heap
        return min_value
    
    def _heapify_down(self, index):
        """
        Restores the MinHeap property by bubbling down the element at `index`.
        """
        size = self.size()
        while self._left_child(index) < size:
            # Get left and right index
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            
            # Find the smaller of the two children
            smallest_index = left_index
            if right_index < size and self._heap[right_index] < self._heap[left_index]:
                smallest_index = right_index
            
            # Swap if current is greater than the smallest child
            if self._heap[index] > self._heap[smallest_index]:
                self._swap(index, smallest_index)
                index = smallest_index
            else:
                break

if __name__ == "__main__":
    min_heap = MinHeap()
    for value in [50, 10, 15, 20, 30, 40]:
        min_heap.insert(value)

    print("Before extract:", min_heap._heap)
    print("Extracted:", min_heap.extract())
    print("After extract:", min_heap._heap)
