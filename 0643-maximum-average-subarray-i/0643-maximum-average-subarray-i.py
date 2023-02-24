class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        max_average = float("-inf")
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            
            if i >= k-1:
                max_average = max(max_average,summ/k)
                summ -= nums[left]
                left +=1
            
        return max_average