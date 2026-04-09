class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 1. 設置 dummy node 指向 head，方便處理回傳值
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            # 用前一組的尾巴，走 k 部找到 kth 
            kth = self.getKth(groupPrev,k)
            if kth == None:
                break
            groupNext = kth.next
            cur = groupPrev.next
            prev = groupNext

            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp 
            # groupPrev 是前一組的尾巴，來連我這組反轉之後的頭，也就是 kth
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next
    
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr