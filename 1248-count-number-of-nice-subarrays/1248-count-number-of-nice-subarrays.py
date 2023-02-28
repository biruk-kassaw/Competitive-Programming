class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pref = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                pref.append(0)
            else:
                pref.append(1)            
        prefix = {0:1}
        total = 0
        ans = 0
        for i in range(len(pref)):
            total += pref[i]
            if total - k in prefix:
                ans += prefix[total-k]
            if total in prefix:
                prefix[total] += 1
            else:
                prefix[total] = 1
        return ans