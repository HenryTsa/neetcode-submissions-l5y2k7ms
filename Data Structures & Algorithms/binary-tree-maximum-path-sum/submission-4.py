class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float("-inf")
        
        def dfs(node):
            if not node:
                return 0
            
            left = max(dfs(node.left), 0)   # 負數不要
            right = max(dfs(node.right), 0) # 負數不要
            
            # 經過此節點的最大路徑
            self.res = max(self.res, node.val + left + right)
            
            # 回傳給父節點只能選一邊
            return node.val + max(left, right)
        
        dfs(root)
        return self.res