# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balance = True
        def Dfs(node:Optional[TreeNode])-> int:
            if node == None:
                return 0
            if abs(Dfs(node.left) - Dfs(node.right)) > 1:
                #print("here")
                self.is_balance = False
            depth = max(Dfs(node.left),Dfs(node.right)) + 1
            #print(node.val,depth,abs(Dfs(node.left) - Dfs(node.right)),self.is_balance)
            return depth

        Dfs(root)
        return self.is_balance