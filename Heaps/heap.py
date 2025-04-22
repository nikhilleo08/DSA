from abc import ABC, abstractmethod

class Heap(ABC):
    """ 
    Abstract base class representing a Heap data structure.
    This class provides the foundational utility methods for both MinHeap and MaxHeap.
    It uses an array (list) to represent the complete binary tree.
    """
    def __init__(self):
        """
        Initialize an empty heap using a list.
        """
        self._heap = []
    
    def size(self):
        """
        Returns the number of elements in the heap.
        """
        return len(self._heap)

    def is_empty(self):
        """
        Checks whether the heap is empty.
        """
        return len(self._heap) == 0

    def peek(self):
        """
        Returns the top (min or max) element of the heap without removing it.
        Raises:
            IndexError: if the heap is empty.
        """
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self._heap[0]
    
    # ------- Internal Utility Methods (used by insert and extract) -------
    def parent(self, index):
        """
        Returns the index of the parent of the given index.
        """
        return (index-1)//2
    
    def left_child(self, index):
        """
        Returns the index of the left child of the given index.
        """
        return (2 * index) + 1
    
    def right_child(self, index):
        """
        Returns the index of the right child of the given index.
        """
        return (2 * index) + 2
    
    def has_left(self, index):
        """
        Checks if the current index has a left child.
        """
        return self.left_child(index) < self.size()
    
    def has_left(self, index):
        """
        Checks if the current index has a right child.
        """
        return self.right_child(index) < self.size()
    
    def swap(self, i, j):
        """
        Swaps elements at indices i and j in the heap array.
        """
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
    
    # ------- Abstract Methods (must be implemented by subclasses) -------

    @abstractmethod
    def insert(self, val):
        """
        Inserts a value into the heap and maintains the heap property.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def extract(self):
        """
        Removes and returns the top element of the heap (min or max).
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def _heapify_up(self, index):
        """
        Heapify upwards from the given index (used during insert).
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def _heapify_down(self, index):
        """
        Heapify downwards from the given index (used during extract).
        Must be implemented by subclasses.
        """
        pass

