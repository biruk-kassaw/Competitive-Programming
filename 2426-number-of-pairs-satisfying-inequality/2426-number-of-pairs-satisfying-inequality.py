class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        q = [nums1[i]-nums2[i] for i in range(n)]
        ans = 0
        def merge(s):
            o = len(s)
            if o==1:
                return s
            nonlocal ans
            m = o//2
            x = merge(s[:m])
            y = merge(s[m:])
            b = len(y)
            for i in x:
                ans += b-bisect_left(y,i-diff)
            return sorted(x+y)
        merge(q)
        return ans