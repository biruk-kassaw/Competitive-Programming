# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        stack = []
        def preorder(node):
            if not node:
                return
            
            stack.append(str(node.val))
            if not node.left and not node.right:
                return
            
            stack.append("(")
            preorder(node.left)
            stack.append(")")
            
            if node.right:
                stack.append("(")
                preorder(node.right)
                stack.append(")")
                
        preorder(root)
        return "".join(stack)