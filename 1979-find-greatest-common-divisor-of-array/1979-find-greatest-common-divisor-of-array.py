class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        
        _min = nums[0]
        _max = nums[0]
        for num in nums:
            if num < _min:
                _min = num
            if num > _max:
                _max = num
                
        return gcd(_min, _max)
        