# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.val = 0
        def helper(root, k):
            if not root:
                return
            helper(root.left,k)
            self.count += 1
            if self.count == k:
                self.val =  root.val
            helper(root.right,k)
        helper(root,k)
        return self.val