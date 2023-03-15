# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = {}
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root):
            if not root:
                return
            helper(root.left)
            self.res[root.val] = self.res.get(root.val, 0) + 1
            helper(root.right)
        helper(root)
        mode = []
        sorted_res = sorted(self.res.items(), key=lambda x:x[1], reverse=True)
        for count in sorted_res:
            if not mode:
                mode.append(count[0])
            elif self.res[mode[-1]] == count[1]:
                mode.append(count[0])
            else:
                break
        return mode
        