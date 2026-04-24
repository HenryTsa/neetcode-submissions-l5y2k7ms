# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # DFS 記住是否有兩個值 BST
        while True:
            if (root.val - p.val) *  (root.val - q.val) <= 0:
                return root
            elif root.val < p.val:
                root = root.right
            else:
                root = root.left
        return None

            

        
        