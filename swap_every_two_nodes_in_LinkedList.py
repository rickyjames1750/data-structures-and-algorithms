"""
Swap Every Two Nodes in a Linked List 

Provided a linked list, swap the position of the 1st and 2nd node, 
then swap the position of the 3rd and 4th node etc.  

"""

class Node: 
    def __init__(self, value, next=None):
        # value 
        self.value = value
        # pointer 
        self.next = next 

    def __repr__(self):
        return f"{self.value}, ({self.next.__repr__()})"
    
def swap_every_two(llist):

llist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(swap_every_two(llist))

