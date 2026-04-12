class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 # 用來存全域最大直徑

        def dfs(node):
            if not node:
                return 0
            
            # 遞迴算出左、右子樹的高度
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 【關鍵】在算高度的同時，順便更新直徑
            # 直徑 = 左邊深度 + 右邊深度
            self.res = max(self.res, left + right)
            
            # 回傳給上一層：目前的深度（左右取大的 + 1）
            return max(left, right) + 1

        dfs(root)
        return self.res