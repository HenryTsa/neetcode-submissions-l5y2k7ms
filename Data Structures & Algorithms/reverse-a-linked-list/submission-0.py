# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        tempt = None
        # 0 -> 1 -> 2 -> 3
        # 0 <- 1 
        while cur != None:
            tempt = cur.next
            cur.next = prev
            prev = cur 
            cur = tempt

        return prev