# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            diameter = self.find_length(node.left) + self.find_length(node.right)  
            res = max(res,diameter)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        #print(root.val,depth)
        return res
    def find_length(self,root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        depth = max(self.find_length(root.left),self.find_length(root.right)) + 1
        return depth
        