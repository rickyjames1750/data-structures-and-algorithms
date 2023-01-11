# Definition for singly-linked list.
# class ListNode:
# def __init__(self, x):
#     self.val = x
#     self.next = None

class Solution: 
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        interval = 1
        while interval < len(lists): # log(k) times 
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]


    def merge2Lists(self, l1, l2):
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            if not l1:
                curr.next = l2
            else: 
                curr.next = l1
            return dummy.next
