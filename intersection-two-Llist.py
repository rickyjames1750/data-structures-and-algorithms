"""
Intersection of two Linked Lists 

Definition for singly-linked list.
class ListNode(object):
    self.val = x
    self.next = None

"""

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :rtype head1, head1, ListNode
        :rtype: ListNode

        """

        def length(head):
            if not head:
                return 0
            return 1 + length(head.next)

        lenA, lenB = length(headA), length(headB)
        currA, currB = headA, headB
        if lenA > lenB:
            for _ in range(lenA-lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next

        while currA != currB:
            currA = currA.next
            currB = currB.next
        return currA
