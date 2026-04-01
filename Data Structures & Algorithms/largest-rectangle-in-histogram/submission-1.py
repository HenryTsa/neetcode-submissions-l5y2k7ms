class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # find Rec = min(Bar1,Bar2)*Bar2-Bar1+1 or height[i]
        # find min value between i->j in O(N)
        # [ 7 1 7 2 2 4 ]
        # consider right boundary = len(height)-1 persume
        # right boundary -> find first right < i th I know -> 
        # i = 0 stack [ 7 ]     
        # i = 1 stack [ 7 1 ] r0 = 1
        # i = 2 stack [ 7 1  ]
        max_area = 0
        right_stack = []
        left_stack = []
        right_boundary = [len(heights)]*len(heights) 
        left_boundary = [-1]*len(heights)
        for i in range(len(heights)):
            #print(right_stack,i)
            while right_stack and heights[right_stack[-1]] > heights[i]:
                #print("hee")
                right_boundary[right_stack.pop()] = i
            right_stack.append(i)
        #print(right_boundary)
        for i in range(len(heights)-1 , -1 , -1):
            while left_stack and heights[left_stack[-1]] > heights[i]:
                left_boundary[left_stack.pop()] = i
            left_stack.append(i)
        #print(left_boundary)

        for i in range(len(heights)):
            max_area = max((right_boundary[i] - left_boundary[i] - 1) * heights[i],max_area)
        return max_area