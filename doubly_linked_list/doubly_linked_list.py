"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    # create instance of ListNode with value
    # increment the DLL length attribute
    # if DLL is empty
        # set head and tail to the new node instance
        
    # if DLL is not empty
        # set new node's next to current head
        # set head's prev to new node
        # set head to the new node

    def add_to_head(self, value):
        new_node = ListNode(value, None)
        self.length += 1

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if(self.head):
            current = self.head
            if self.head is self.tail:
                self.tail = None
            self.head = current.next
            self.length -= 1
            return current.value
    
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create instance of ListNode with value
        new_node = ListNode(value, None)
        # increment the DLL length attribute
        self.length += 1
        # if DLL is empty
        if not self.head and not self.tail:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
        else:
        # if DLL is not empty
            # set new node's prev to current tail
            new_node.prev = self.tail
            # set tail's next to new node
            self.tail.next = new_node
            self.tail = new_node

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        curr_tail = self.tail
        if curr_tail.prev:
            self.tail = curr_tail.prev
            new_tail = curr_tail.prev
            new_tail.value = None
        else:
            self.tail = None
            self.head = None
        self.length -= 1
        return curr_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        current = self.head
        while current != node:
            current = current.next
        if current.prev:
            before = current.prev
            before.next = current.next
        if current.next:
            after = current.next
            after.prev = current.prev

        prev_head = self.head
        prev_head.prev = current
        current.next = prev_head
        current.prev = None
        self.head = current
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        current = self.head
        while current != node:
            current = current.next
        if current.prev:
            before = current.prev
            before.next = current.next
            if node == self.tail:
                self.tail = before
        if current.next:
            after = current.next
            after.prev = current.prev
            if node is self.head:
                self.head = after

        prev_tail = self.tail
        prev_tail.next = current
        current.prev = prev_tail
        current.next = None
        self.tail = current 

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        current = self.head
        while current != node:
            current = current.next
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        if current.prev:
            before = current.prev
            before.next = current.next
            if node == self.tail:
                self.tail = before
        if current.next:
            after = current.next
            after.prev = current.prev
            if node == self.head:
                self.head = after
        self.length -= 1


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head
        item = 0
        while current:
            if current.value > item:
                item = current.value
            current = current.next

        return item