# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = nth_ptr  =  ListNode(-1)
        nth_ptr.next = head
        cur.next = head
        for i in range(n):
            if nth_ptr:
                nth_ptr = nth_ptr.next
        #print(nth_ptr.val)
        prev = None
        while nth_ptr :
            prev = cur
            cur = cur.next
            nth_ptr = nth_ptr.next
        if prev.val != -1:
            prev.next = cur.next
            return head
        else:
            return cur.next

        