# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def helper(node, count):
            
            if node == None:
                return count
            c_left = helper(node.right,count + 1)
            c_right = helper(node.left, count + 1)
            return max(depth,c_left, c_right)
        
        return helper(root, depth)