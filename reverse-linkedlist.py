
"""

Definition for singly-linked list.
class ListNode: 
    self.val = x 
    self.next = None
    
"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head 
        while (curr != None):
            temp = curr.next
            curr.next = prev 
            prev = curr 
            curr = temp
        return prev 