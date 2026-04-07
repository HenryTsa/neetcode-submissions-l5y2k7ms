# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        min_heap = []
        cur = dummy
        min_value = {}
        for i , ptr in enumerate((lists)):
            if ptr:
                heapq.heappush(min_heap,(ptr.val,i,ptr))
        while min_heap:
            cur_tuple = heapq.heappop(min_heap)
            cur.next = cur_tuple[2]
            cur = cur.next
            if cur_tuple[2].next:
                next_node = cur_tuple[2].next 
                heapq.heappush(min_heap,(next_node.val,cur_tuple[1],next_node))
        return dummy.next
