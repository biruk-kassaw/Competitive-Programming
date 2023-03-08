# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        seen = deque()
        seen.append((root, 1))
        maxLen = 1
        
        while seen:
            maxLen = max(maxLen, seen[-1][1] - seen[0][1] + 1)
            n = len(seen)
            
            for i in range(n):
                tmp = seen.popleft()
                node = tmp[0]
                dist = tmp[1]
                if node.left: 
                    seen.append((node.left, 2*dist))
                if node.right: 
                    seen.append((node.right, 2*dist+1))
        
        return maxLen