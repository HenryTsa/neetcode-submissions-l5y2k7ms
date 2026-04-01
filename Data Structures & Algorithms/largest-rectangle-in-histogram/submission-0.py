class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # find Rec = min(Bar1,Bar2)*Bar2-Bar1+1 or height[i]
        max_area = 0
        for i in range(len(heights)):
            max_area  = max(max_area,heights[i])
        print(max_area)
        
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                min_height = float('inf')
                for k in range(i,j+1):
                    min_height = int(min(min_height,heights[k]))
                max_area = max(min_height*(j-i+1),max_area)

        return max_area