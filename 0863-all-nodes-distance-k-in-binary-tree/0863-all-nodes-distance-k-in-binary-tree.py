# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def findTarget(self, root, target):
        q = deque([(root)])
        res = None
        while q:
            cur = q.popleft()
            if cur.val == target.val:
                res = cur
                
            if cur.left:
                cur.left.parent = cur
                q.append(cur.left)
            if cur.right:
                cur.right.parent = cur
                q.append(cur.right) 
        return res
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        target_node = self.findTarget(root, target)
        q = deque([(target_node, 0)])
        ans = []
        visited = set()
        
        while q:
            node, distance = q.popleft()
            visited.add(node)
            if distance > k:
                break
                
            if distance == k:
                ans.append(node.val)
                
            if node.right and node.right not in visited:
                q.append((node.right, distance+1))
                
            if node.left and node.left not in visited:
                q.append((node.left, distance+1))
                
            if node != root and node.parent and node.parent not in visited:
                q.append((node.parent, distance+1))
                
        return ans   
        