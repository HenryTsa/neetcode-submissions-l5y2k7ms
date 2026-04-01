class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        # 只要 l1 或 l2 還有值，或者還有進位沒處理完，就繼續
        while l1 or l2 or carry:
            # 1. 取值（如果已經到底了就當作 0）
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # 2. 計算總和與進位
            val = v1 + v2 + carry
            carry = val // 10  # 更新進位 (1 或 0)
            val = val % 10     # 當前位數的值
            
            # 3. 建立新節點並接上去
            curr.next = ListNode(val)
            
            # 4. 移動指針
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next