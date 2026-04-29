# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = float("-inf")
        if root == None:
            return 0
        self.find_path(root)
        return self.max_val

        
    def find_path(self,root):
        if root == None:
            return 0
        left_del = self.find_path(root.left)
        right_del = self.find_path(root.right)
        path = max(root.val+left_del + right_del,root.val+left_del,root.val+right_del,root.val)    
        self.max_val = max(path,self.max_val)
        delicate_parent = max(root.val + left_del,root.val + right_del,root.val)
        return delicate_parent
        