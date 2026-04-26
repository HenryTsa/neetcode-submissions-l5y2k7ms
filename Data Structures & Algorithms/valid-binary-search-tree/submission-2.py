class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # stack 存 (節點, 下界, 上界)
        stack = [(root, float("-inf"), float("inf"))]
        
        while stack:
            node, lower, upper = stack.pop()
            
            if not (lower < node.val < upper):
                return False
            
            if node.left:
                stack.append((node.left, lower, node.val))
            if node.right:
                stack.append((node.right, node.val, upper))
        
        return True