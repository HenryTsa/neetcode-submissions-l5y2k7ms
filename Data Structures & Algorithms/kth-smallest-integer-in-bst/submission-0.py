# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_all_descent(self,root):
        if root == None:
            return 0
        return  1 + self.find_all_descent(root.left) + self.find_all_descent(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if root == None:
            return 0
        tmp = root
        left_descent = self.find_all_descent(tmp.left)
        #print(root.val,k,left_descent)
        if  left_descent == k-1:
            #print("1")
            return tmp.val
        elif left_descent >= k:
            #print("2")
            return self.kthSmallest(tmp.left,k)
        elif left_descent < k:
            #print("3")
            return self.kthSmallest(tmp.right,k-left_descent-1)
        return 0