class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if (str(nums[j]) + str(nums[j-1])) > (str(nums[j-1]) + str(nums[j])) :
                    temp = nums[j]
                    nums[j] = nums[j-1]
                    nums[j-1] = temp
                    
        output = [str(x) for x in nums]
        s = ''
        return str(int((s.join(output))))
