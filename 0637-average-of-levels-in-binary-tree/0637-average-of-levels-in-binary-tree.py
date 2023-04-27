# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avg = []
        queue = deque([root])
        
        while queue:
            n = len(queue)
            _sum = 0
            for i in range(n):
                cur = queue.popleft()
                _sum += cur.val
                
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            avg.append(_sum/n)
        return avg