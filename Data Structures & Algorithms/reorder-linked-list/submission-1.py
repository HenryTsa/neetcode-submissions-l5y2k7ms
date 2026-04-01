# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def checklist(self,head):
        i = 0
        print("here")
        lst = []
        while head!=None and i <= 3:
            i += 1
            lst.append(head.val)
            head = head.next
        print(lst)

    def reorderList(self, head: Optional[ListNode]) -> None:
        
        reverse_head = ListNode()
        n = 0
        cur = ListNode()
        cur.next = head
        while cur != None:
            cur = cur.next
            if cur!= None:
                n += 1
        if n == 1:
            return 
        half = (n + 1) //2
        reverse_head.next = head
        for i in range(half):
            reverse_head = reverse_head.next
            #print(reverse_head.val)        
        prev = None
        tempt = reverse_head.next
        reverse_head.next = None
        reverse_head = tempt
        nxt = reverse_head.next
        while reverse_head != None:
            #print(reverse_head.val)
            reverse_head.next = prev
            prev = reverse_head
            reverse_head = nxt
            if reverse_head:
                nxt = reverse_head.next
        cur = ListNode()
        tempt_head = head
        #self.checklist(prev)
        #self.checklist(head)
        while prev or  tempt_head:
            if tempt_head:
                tempt_left = tempt_head.next
                cur.next = tempt_head
                cur = cur.next
                tempt_head = tempt_left
            if prev:
                tempt_right = prev.next
                cur.next = prev
                cur = cur.next
                prev = tempt_right
            
            

            


        

        