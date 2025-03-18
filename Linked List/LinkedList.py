class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


arr = [40, 6, 3, 1, 7, 20, 3, 3, 3, 1, 5]


def createLinkedListFromArray(arr: list):
    if len(arr) == 0:
        print('Please enter an arr of length atleast 1.')
        return None
    node_at_0 = Node(arr[0])
    head = node_at_0
    mover = node_at_0
    tail = None
    for i in range(1, len(arr)):
        temp_node = Node(arr[i])
        mover.next = temp_node
        mover = temp_node
    tail = mover
    return (head, tail)


ans = createLinkedListFromArray(arr)
print('Original Array', arr)
print(f'Head: {ans[0].val}, Tail: {ans[1].val}')


# def traverseLinkedList(head: Node):
#     temp = head
#     while temp:
#         print('VALUE', temp.val)
#         temp = temp.next


# traverseLinkedList(ans[0])

print()
print('Traversal of Linked List is as follows.')


def traverseLinkedList(head: Node):
    temp = head
    while temp:
        if temp.next:
            print(temp.val, end='=>')
        else:
            print(temp.val)
        temp = temp.next
    print()


traverseLinkedList(ans[0])


def lengthOfLinkedList(head: Node):
    temp = head
    cnt = 0
    while temp:
        cnt += 1
        temp = temp.next
    return cnt


print('Length of Linked List is', lengthOfLinkedList(ans[0]))
print()

print('Search in the Linked List')


def searchInLinkedList(head: Node, val: int):
    temp = head
    while temp:
        if temp.val == val:
            return True
        temp = temp.next
    return False


search_el = 5
is_present = searchInLinkedList(ans[0], search_el)
print(f"Value {search_el} {'is present' if is_present else 'is not present' } in the Linked List")

search_el = 100
is_present = searchInLinkedList(ans[0], search_el)
print(f"Value {search_el} {'is present' if is_present else 'is not present' } in the Linked List")


# Deleting a node from the Linked List
# First
# Last
# Position
# Value

print()
print('Remove Nodes from LinkedList')
print('1) Remove Head Node')


def removeHeadNode(head: Node):
    if head is None:
        return head

    temp = head
    head = head.next
    del temp
    return head


new_head_remove_head = removeHeadNode(ans[0])
traverseLinkedList(new_head_remove_head)


print('2) Remove Tail Node')


def removeTailNode(head: Node):
    if head is None:
        return head
    if head.next is None:
        del head
        return None

    temp = head
    while temp.next.next is not None:
        temp = temp.next

    del temp.next
    temp.next = None
    return head


new_head_remove_tail = removeTailNode(new_head_remove_head)
traverseLinkedList(new_head_remove_tail)


print('3) Remove Node at given Position')


def removeIthNode(head: Node, pos: int):
    length = lengthOfLinkedList(head)

    if pos > length-1:
        print("Position is greater than length of Linked List: ", length)
        return head

    if pos < 0:
        print("Invalid Position: ", pos)
        return head

    if pos == 0:
        return removeHeadNode(head)

    temp = head
    cnt = 0
    while cnt < pos-1:
        temp = temp.next
        cnt += 1
    next_node = temp.next
    temp.next = next_node.next
    del next_node
    return head


new_head_remove_ith_pos = removeIthNode(new_head_remove_tail, 0)
print('Removing Element at Pos 0')
traverseLinkedList(new_head_remove_ith_pos)

print('Removing Element at Pos 2')
new_head_remove_ith_pos = removeIthNode(new_head_remove_ith_pos, 2)
traverseLinkedList(new_head_remove_ith_pos)

print('Removing Element at Pos 6 i.e tail node')
new_head_remove_ith_pos_new = removeIthNode(new_head_remove_ith_pos, 6)
traverseLinkedList(new_head_remove_ith_pos_new)

print('Removing Element at Pos 8')
new_head_remove_ith_pos_new = removeIthNode(new_head_remove_ith_pos, 8)
traverseLinkedList(new_head_remove_ith_pos_new)

print('Removing Element at Pos -4')
new_head_remove_ith_pos_invalid = removeIthNode(new_head_remove_ith_pos, -4)
traverseLinkedList(new_head_remove_ith_pos_invalid)


print('4) Remove Node with given Value')


def removeNodeWithVal(head: Node, val: int):
    if head is None:
        return head

    if head.val == val:
        curr = head # To delete
        head = head.next
        prev = head
        temp = head.next
        del curr

    prev = head
    temp = head.next
    while temp.next:
        if temp.val == val:
            curr = temp # To delete
            temp = temp.next
            prev.next = temp
            del curr
        else:
            prev = temp
            temp = temp.next

    if temp.next is None and temp.val == val:
        prev.next = None
        del temp 
    return head


new_head_remove_val = removeNodeWithVal(new_head_remove_ith_pos_new, 3)
traverseLinkedList(new_head_remove_val)


print()
print('Insert Nodes into LinkedList')
print('1) Insert Node at Head')


def insertNodeAtHead(head: Node, val: int):
    new_node = Node(val)
    if head is None:
        return new_node
    curr = head
    new_node.next = curr
    head = new_node
    return head


new_arr = [10]
new_head, new_tail = createLinkedListFromArray(new_arr)

inserted_head = insertNodeAtHead(new_head, 50)
traverseLinkedList(inserted_head)


print('2) Insert at Tail Node')


def insertAtTailNode(head: Node, val: int):
    if head is None or head.next is Node:
        return Node(val)

    curr: Node = head
    while curr.next:
        curr = curr.next

    new_node = Node(val)
    curr.next = new_node
    return head


new_head_insert_tail = insertAtTailNode(inserted_head, 55)
traverseLinkedList(new_head_insert_tail)


print('3) Insert Node at given Position')


def insertAtPosition(head: Node, pos: int, val: int):
    length = lengthOfLinkedList(head)

    if pos > length:
        print(f'Position should be between 0-{length}')
        return head
    if pos < 0:
        print("Invalid Position: ", pos)
        return head

    if pos == 0:
        return insertNodeAtHead(head, val)

    temp = head
    cnt = 0
    while temp:
        cnt += 1
        if cnt == pos:
            new_node = Node(val)
            new_node.next = temp.next
            temp.next = new_node
            break
        temp = temp.next
    return head


# Beginning
new_head_insert_ith_pos = insertAtPosition(new_head_insert_tail, 0, 57)
print('Inserting Element at Pos 0')
traverseLinkedList(new_head_insert_ith_pos)

# Middle
print('Inserting Element at Pos 2')
new_head_insert_ith_pos = insertAtPosition(new_head_insert_ith_pos, 2, 75)
traverseLinkedList(new_head_insert_ith_pos)

# Tail
print('Inserting Element at Pos 5')
new_head_insert_ith_pos = insertAtPosition(new_head_insert_ith_pos, 5, 1)
traverseLinkedList(new_head_insert_ith_pos)

# Prints message that pos should be between 0-lengthOfLinkedList 
print('Inserting Element at Pos greater than length')
new_head_insert_ith_pos = insertAtPosition(new_head_insert_ith_pos, 7, 100)
traverseLinkedList(new_head_insert_ith_pos)


print('4) Insert Node before given value')


def insert_node_before_given_val(head: Node, val: int, new_node_val: int):
    if head is None:
        return head

    if head.val == val:
        new_node = Node(val)
        new_node.next = head 
        head = new_node
        return head

    temp = head.next
    while temp.next:
        if temp.next.val == val:
            new_node = Node(new_node_val)
            new_node.next = temp.next
            temp.next = new_node
            break
        else:
            temp = temp.next
    return head


new_head_remove_val = insert_node_before_given_val(new_head_insert_ith_pos, 10, 48)
traverseLinkedList(new_head_remove_val)
