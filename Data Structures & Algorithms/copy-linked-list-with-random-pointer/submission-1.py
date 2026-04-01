"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def check(self,head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print(res)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = cur = Node(0)
        first = True
        cur = head
        prev = None
        dic = defaultdict(list)
        while cur :
            tem = Node(cur.val)
            dic[cur] = tem
            cur = cur.next
            if first:
                first = False
                dummy.next = tem
            if prev:
                prev.next = tem
            prev = tem
            tem.next = None
        cur = head
        cur_new = dummy.next
        while cur:
            if cur.random:
                cur_new.random = dic[cur.random]
            cur = cur.next
            cur_new = cur_new.next

        #print(dic)
        #self.check(dummy.next)

        return dummy.next