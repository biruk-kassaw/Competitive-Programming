class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        ans = set()
        def primeFactor(n):
            d = 2
            while d*d <= n:
                while n % d == 0:
                    ans.add(d)
                    n //= d
                d += 1
            if n > 1:
                ans.add(n)
        for num in nums:
            primeFactor(num)
            
        return len(ans)
    