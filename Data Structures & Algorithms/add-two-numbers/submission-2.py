# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        str1 = []
        str2 = []
        while cur1 or cur2:
            if cur1:
                str1.append(str(cur1.val))
                cur1 = cur1.next
            if cur2:
                str2.append(str(cur2.val))
                cur2 = cur2.next
        #print(str1,str2)
        for i in range(len(str1)//2):
            tem1 = str1[i]
            str1[i] = str1[len(str1)-1-i]
            str1[len(str1)-1-i] = tem1
        for i in range(len(str2)//2):
            tem2 = str2[i]
            str2[i] = str2[len(str2)-1-i]
            str2[len(str2)-1-i] = tem2
        str1 = "".join(str1)  
        str2 = "".join(str2)
        #print(str1,str2)
        res = int(str1)+int(str2)
        #print(res)
        dummy = ListNode()
        prev = None
        if res == 0:
            return ListNode(0)
        while res != 0:
            cur = ListNode(res%10)
            if prev==None:
                dummy.next = cur
            else:
                prev.next = cur
            res = res//10
            prev =cur 
        return dummy.next



