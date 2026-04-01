# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = defaultdict(ListNode)
        dummy = ListNode()
        dummy.next = cur = head
        while cur != None:
            if cur in dic:
                return True
            dic[cur] = 0
            cur = cur.next
        return False