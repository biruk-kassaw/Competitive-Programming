# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dia(root):
            nonlocal ans
            if not root:
                return 0
            
            left = dia(root.left)
            right = dia(root.right)
            ans = max(ans, left + right)
            
            return 1 + max(right,left)
        dia(root)
        return ans