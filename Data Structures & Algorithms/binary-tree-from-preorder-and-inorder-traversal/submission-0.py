# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_index(self,arr,val):
        for i in range(len(arr)):
            if arr[i] == val:
                return i
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        mid = self.find_index(inorder, root_val)
        
        # mid 就是左子樹的元素個數，直接用它切割
        root.left = self.buildTree(
            preorder[1 : mid + 1],   # 左子樹有 mid 個元素
            inorder[0 : mid]
        )
        root.right = self.buildTree(
            preorder[mid + 1 :],     # 剩下全是右子樹
            inorder[mid + 1 :]
        )
        
        return root