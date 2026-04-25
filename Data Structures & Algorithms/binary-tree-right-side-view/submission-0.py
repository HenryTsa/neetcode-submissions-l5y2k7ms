# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        level_num = 0
        if root:
            q.append(root)
            level_num = 1
        while q:
            level_element = []
            next_level_num = 0
            for i in range(level_num):
                tmp = q.popleft()
                level_element.append(tmp.val)
                if tmp.left:
                    q.append(tmp.left)
                    next_level_num += 1
                if tmp.right:
                    q.append(tmp.right)
                    next_level_num += 1
            level_num = next_level_num
            res.append(level_element[-1])
        return res