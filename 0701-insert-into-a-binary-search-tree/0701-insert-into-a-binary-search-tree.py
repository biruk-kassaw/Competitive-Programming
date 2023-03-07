# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def helper(root):
            
            if root.val > val :
                if not root.left:
                    root.left = TreeNode(val)
                    return 
                helper(root.left)
            if root.val < val:
                if not root.right:
                    root.right = TreeNode(val)
                    return
                helper(root.right)
        if not root:
                return TreeNode(val)
        helper(root)
        return root