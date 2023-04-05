class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            cur = nums[i]
            for j in range(i, n):
                cur = math.gcd(cur, nums[j])
                if cur == k:
                    ans += 1
                elif cur < k:
                    break
        return ans