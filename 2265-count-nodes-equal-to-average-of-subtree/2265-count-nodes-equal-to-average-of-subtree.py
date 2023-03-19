# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return [0,0]
            left = helper(root.left)
            right = helper(root.right)

            total = (left[0] + right[0] + root.val)
            count = (left[1] + right[1] + 1)
            avg = int(total/count)
            if avg == root.val:
                self.res += 1
            return [total, count]
        helper(root)
        return self.res