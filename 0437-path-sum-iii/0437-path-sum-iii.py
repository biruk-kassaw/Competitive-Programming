# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
        self.sums = {0:1}
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def helper(root, summ):
            if not root:
                return
            
            local_sum = summ  + root.val
            
            if (local_sum - targetSum) in self.sums:
                self.ans += self.sums[local_sum - targetSum]
            
            self.sums[local_sum] = self.sums.get(local_sum, 0) + 1
            
            helper(root.left, local_sum)
            helper(root.right, local_sum)
            self.sums[local_sum] -= 1
            
        helper(root, 0)
        return self.ans