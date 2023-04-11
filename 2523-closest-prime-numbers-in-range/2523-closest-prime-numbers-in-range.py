class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True] * (right+1)
        d = 2
        is_prime[0] = is_prime[1] = False
        
        while d * d <= right + 1:
            if is_prime[d]:
                i = d + d
                while i <= right:
                    is_prime[i] = False
                    i += d
            d += 1
        ans = [-1, -1]
        nums1 = -1
        nums2 = -1
        
        for i in range(left, right + 1):
            if is_prime[i]:
                if nums1 == -1:
                    nums1 = i
                    ans[0] = i
                    
                elif nums2 == -1:
                    nums2 = i
                    ans[1] = i
                    
                else:
                    if i - nums2 < ans[1] - ans[0]:
                        ans = [nums2, i]
                    nums2 = i
                    
        return [-1, -1] if ans[0] == -1 or ans[1] == -1 else ans
        
        