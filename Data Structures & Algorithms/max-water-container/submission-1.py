class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        cur_area = 0
        left_idx,right_idx = 0,len(heights)-1
        while left_idx < right_idx:
            cur_area = (right_idx - left_idx)*min(heights[right_idx],heights[left_idx])
            if heights[left_idx] < heights[right_idx]:
                left_idx += 1
            elif heights[left_idx] > heights[right_idx]:
                right_idx -= 1
            else:
                if heights[left_idx+1]> heights[right_idx-1]:
                    left_idx += 1
                else:
                    right_idx -=1
            max_area = max(max_area,cur_area)
        return max_area
