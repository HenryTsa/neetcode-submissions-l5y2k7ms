# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 我用一個 dic 紀錄從 root 到此點最大值
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        stack = []
        dic = {}
        stack.append(root)
        dic[root] = root.val
        while stack:
            tmp = stack.pop()
            if tmp.val == dic[tmp]:
                res += 1
            if tmp.left:
                stack.append(tmp.left)
                dic[tmp.left] = max(dic[tmp],tmp.left.val)
            if tmp.right:
                stack.append(tmp.right)
                dic[tmp.right] = max(dic[tmp],tmp.right.val)

        return res

        