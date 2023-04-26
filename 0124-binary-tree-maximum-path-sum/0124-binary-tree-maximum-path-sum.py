# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            
            left_sum = max(left_sum, 0)
            right_sum = max(right_sum, 0)
            
            split_sum = left_sum + right_sum + root.val
            
            max_path[0] = max(max_path[0], split_sum)
            
            return root.val + max(left_sum, right_sum)
        dfs(root)
        return max_path[0]