"""

Remove Duplicate from Linked List

Given a sorted linked list of integers, remove all duplicate elements in the 
linked list so that all elements in the linked list are unique. 

Here's an example and some starter code:


"""

class Node:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next 

    def __repr__(self):
        return f"({self.value}, {self.next})"

    def remove_dup(lst):
        # Fill this with remove dup 
        curr = lst
        while curr and curr.next:
            if curr.value == curr.next.value:
                curr.next = curr.next.next # skip to 2
            else: 
                curr = curr.next

    lst = Node(1, Node(2, Node(2, Node(2, Node(3, Node(3)))))) 




    remove_dup(lst)   
    print(lst)
    # (1, 2, 3, [3, None]) 