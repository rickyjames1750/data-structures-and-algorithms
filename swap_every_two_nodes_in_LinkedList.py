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
    # Not really necessary more for aesthetic 
    head = llist

    # Initialize our current pointer to the head
    curr = head
    # Iterate through the list
    while curr is not None and curr.next is not None:
        curr.value, curr.next.value = curr.next.value, curr.value
        curr = curr.next.next

    return head

llist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(swap_every_two(llist))

