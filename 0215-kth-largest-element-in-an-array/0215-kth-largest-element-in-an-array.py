class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = [4]
        def quickSort(left, right):
            
            if left > right:
                return
            
            p = sortPivot(left, right)
            
            if p == (len(nums)-k):
                ans[0] = nums[len(nums)-k]
                return
            
            quickSort(left, p-1)
            
            quickSort(p + 1, right)
            
        def sortPivot(left, right):
            smaller = left
            
            for i in range(left, right):
                if nums[i] < nums[right]:
                    nums[smaller], nums[i] = nums[i], nums[smaller]
                    smaller += 1
            nums[right], nums[smaller] = nums[smaller], nums[right]
            
            return smaller
        
        quickSort(0, len(nums)-1)
        
        return ans[0]
    
    
    
    
    