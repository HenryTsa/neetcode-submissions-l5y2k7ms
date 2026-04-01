class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 🌟 步驟一：保命符！確保 nums1 永遠是比較短的那條蛋糕
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        
        # 定義 Binary Search 的範圍 (注意：是對「切線位置」做搜尋，所以是 0 到 m)
        l, r = 0, m
        
        # 左半部總共需要幾個數字？ (加 1 是為了讓奇數時，左邊多拿一個)
        half_len = (m + n + 1) // 2
        
        while l <= r:
            # i 是 nums1 的切線 (拿了幾個)；j 是 nums2 的切線 (連動算出來的)
            i = (l + r) // 2
            j = half_len - i
            
            # 🌟 步驟二：召喚四大護法與極限魔法 (越界就給無限大/無限小)
            A_left  = float('-inf') if i == 0 else nums1[i - 1]
            A_right = float('inf')  if i == m else nums1[i]
            
            B_left  = float('-inf') if j == 0 else nums2[j - 1]
            B_right = float('inf')  if j == n else nums2[j]
            
            # 🌟 步驟三：交叉比對，審判這刀切得對不對
            if A_left <= B_right and B_left <= A_right:
                # 🔪 完美的一刀出現了！開始結算成績
                
                # 情況 A：總長度是奇數 -> 答案就是左半部的霸主
                if (m + n) % 2 == 1:
                    return float(max(A_left, B_left))
                
                # 情況 B：總長度是偶數 -> 左邊霸主 + 右邊最小的，加起來除以 2
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            
            # 🌟 步驟四：如果不完美，調整切線方向
            elif A_left > B_right:
                # A 左邊的數字太大了！代表 nums1 切太多了，切線必須往左退
                r = i - 1
            else:
                # B_left > A_right (B 左邊太大了，代表 nums1 切太少了)，切線必須往右進
                l = i + 1