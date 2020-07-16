"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert value here
            if self.left is None:
               self.left = BSTNode(value)
            else:
                # Repeat the process on left subtree
                self.left.insert(value)
                # Case 2: value is greater than or equal self.value
        elif value >= self.value:
            # If there is no right child, insert value here
            if self.right is None:
               self.right = BSTNode(value)
            else:
                # Repeat the process on right subtree   
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value 
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        elif self.right is None:
                return False
        else:
            return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        #we know the max value will never be in the self.left
        if not self.right: # if max_value is not in self.right. This could also be if self.right is None:
            return self.value # return node value
        else:
            return self.right.get_max() # return the max_value from self.right w/ recursion


    # Call the function `fn` on the value of each node
    def for_each(self, fn): #This is DFT traversal
        # recursive solution
        fn(self.value) #calling the fn function on the value of each node
        if self.left:
            self.left.for_each(fn) #printing each value on the left
        if self.right:
            self.right.for_each(fn)#printing each value on the right

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self is None:
            return
        
        if self.left is not None:
            self.left.in_order_print()

        print(self.value)

        if self.right is not None:
            self.right.in_order_print()


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node): #use queues (FIFO)
        queue = Queue()

        queue.enqueue(node)
        
        while (len(queue) > 0):

            queue_deq = queue.dequeue()

            print(queue_deq.value)
         
            if queue_deq.left is not None:
                queue.enqueue(queue_deq.left)
    
            if queue_deq.right is not None:
                queue.enqueue(queue_deq.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node): # use stacks
        stack = Stack()

        stack.push(node)
        
        while(stack.size > 0):
            stack_pop = stack.pop()
            print(stack_pop.value)

            if stack_pop.left is not None:
                stack.push(stack_pop.left)

            if stack_pop.right is not None:
                stack.push(stack_pop.right)



    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass