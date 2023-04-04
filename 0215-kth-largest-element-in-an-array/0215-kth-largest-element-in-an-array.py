class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = [4]
        k = len(nums) - k
        
        def quickSort(left, right):
            
            smaller = left
            
            for i in range(left, right):
                if nums[i] <= nums[right]:
                    nums[smaller], nums[i] = nums[i], nums[smaller]
                    smaller += 1
            nums[right], nums[smaller] = nums[smaller], nums[right]
                    
            if smaller < k:
                return quickSort(smaller + 1, right)
            
            elif smaller > k:
                return quickSort(left, smaller - 1)
            
            else:
                return nums[k]
            
        return quickSort(0, len(nums)-1)
        
    
    
    
    