# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # inorder
        if self.isSame(root,subRoot):
            return True
        if root and subRoot:
            if self.isSubtree(root.left ,subRoot) or self.isSubtree(root.right ,subRoot):
                return True
        return False

    def isSame(self,root,subRoot):
        if subRoot==None and root==None:
            return True
        elif root and subRoot: 
            if root.val == subRoot.val:
                return self.isSame(root.left,subRoot.left) and self.isSame(root.right,subRoot.right)
        else:
            return False