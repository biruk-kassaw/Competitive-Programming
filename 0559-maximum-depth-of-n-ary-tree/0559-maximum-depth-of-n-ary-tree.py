"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        ans = [0]
        
        def dfs(node, local_depth):
            if not node:
                return
            
            local_depth += 1
            ans[0] = max(ans[0], local_depth)
            
            for child in node.children:
                dfs(child, local_depth)
            
        dfs(root, 0)
        return ans[0]