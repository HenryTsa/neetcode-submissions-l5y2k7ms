# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balance = True
        def Dfs(node:Optional[TreeNode])-> int:
            nonlocal is_balance 
            if node == None:
                return 0
            Left = Dfs(node.left)
            Right = Dfs(node.right)
            if abs(Left - Right) > 1:
                print("here")
                is_balance = False
            depth = max(Left,Right) + 1
            #print(node.val,depth,abs(Dfs(node.left) - Dfs(node.right)),is_balance)
            return depth

        Dfs(root)
        return is_balance