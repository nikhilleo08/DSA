# What Are Heaps? (Intuition First)
## What is a Heap?
- A Heap is a binary tree (but NOT a Binary Search Tree).
- It is a complete binary tree — meaning all levels are completely filled except possibly the last, which is filled from left to right.
- Heaps follow a specific property:
    - **Max Heap**: Every **parent node** is **greater** than or equal to its children.
    - **Min Heap**: Every **parent node** is **less** than or equal to its children.
- So basically:
    - In Max Heap, the largest element is always at the **top** (root).
    - In Min Heap, the smallest element is at the **top** (root).

## STEP 1 — Basic Heap Representation (Array)
- In memory, a Heap is stored as an array, not as a tree. Here's why:
- Example:
    - Given a complete binary tree like this (Min Heap):
    ```markdown
              5
            /   \
          10     15
         /  \   /
        20  30 40
    ```
    The corresponding array is:
    - [5, 10, 15, 20, 30, 40]
- Parent-Child Index Formula:
    - If a node is at index i:
        - Left child → 2 * i + 1
        - Right child → 2 * i + 2
        - Parent → (i - 1) // 2


## TASK 1 for You: Understand Indexing
- Given heap = [5, 10, 15, 20, 30, 40], tell me:
    - What is the left and right child of index 1 (i.e., element 10)?
        - Ans: 
            - Left Index => (2 * 1) + 1 => 2 + 1 => 3 i.e heap[3] => 20
            - Right Index => (2 * 1) + 2 => 2 + 2 => 4 i.e heap[4] => 30
    - What is the parent of index 4 (i.e., element 30)?
        - Ans:
            - Parent of index **i** is given by (i - 1)//2 i.e floor value, so (i - 1)//2 => (4-1)//2 => 3//2 => 1
            - Therefore parent of index 4 is 1

![alt text](image.png)


## Now Let’s Design the Heap Class (Step 1 of Implementation)

We’ll follow a clean design using OOP and prepare for both MinHeap and MaxHeap types using inheritance and abstraction.

### STEP 1.1: Base Heap Class (Abstract)
- This will:
    - Use an array internally to store elements.
    - Have abstract comparison logic (min/max heap decides this).
    - Be the parent class for MinHeap and MaxHeap.



