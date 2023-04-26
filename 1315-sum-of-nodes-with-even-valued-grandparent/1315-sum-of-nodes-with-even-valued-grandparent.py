# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = [0]
        def dfs(root, is_even_grand, is_even_parent):
            if not root:
                return
            
            if is_even_grand:
                ans[0] += root.val
                
            dfs(root.left, is_even_parent, root.val % 2 == 0)
            
            dfs(root.right, is_even_parent, root.val % 2 == 0)
            
            
        dfs(root, False, False)
        return ans[0]