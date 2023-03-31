# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 1
        current_level = [(root, 1)]
        
        while current_level:
            new_level = []
            
            for node, pos in current_level:
                if node.left:
                    new_level.append((node.left, pos*2))
                    
                if node.right:
                    new_level.append((node.right, (pos*2)+1 ))
            if new_level:
                max_width = max(max_width, new_level[-1][1] - new_level[0][1] + 1)
            
            current_level = new_level
        return max_width