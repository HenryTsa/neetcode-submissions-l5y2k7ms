class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        cur_area = 0
        for i in range(len(heights)-1):
            for j in range(len(heights)):
                cur_area = (j - i) * min(heights[i],heights[j])
                max_area = max(max_area,cur_area)
        return max_area
