# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        dic = {}
        if root:
            stack.append(root)
            # (必須小於，必須大於)
        while stack:
            tmp = stack.pop()
            # 為子代設下條件
            if tmp.left:
                if tmp in dic:
                    dic[tmp.left] = (dic[tmp][0],tmp.val)
                else:
                    dic[tmp.left] = (float("-inf"),tmp.val)
                stack.append(tmp.left)
            if tmp.right:
                if tmp in dic:
                    dic[tmp.right] = (tmp.val ,dic[tmp][1])
                else:
                    dic[tmp.right] = (tmp.val ,float("inf"))
                stack.append(tmp.right)
            # 檢查自己
            if tmp in dic:
                if tmp.val >= dic[tmp][1] or tmp.val <= dic[tmp][0]:
                    return False
            
        return True