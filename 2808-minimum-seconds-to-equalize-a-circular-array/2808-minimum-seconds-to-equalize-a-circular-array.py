class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n - 1  # assuming all numbers are different

        # store all indexes of the same number
        m = {}

        for i, num in enumerate(nums):
            if num not in m:
                m[num] = []
            m[num].append(i)

        for v in m.values():  # traverse all the different numbers
            v.sort()  # Sort the indexes in ascending order
            len_v = len(v)  # size of vector
            # now we change all remaining number = total size of the array - size of the same number
            maxi = (n - 1) - (v[len_v - 1] - v[0])
            for j in range(1, len_v):
                # maximum difference between adjacent indexes
                maxi = max(maxi, v[j] - v[j - 1] - 1)
            # minimize the maximum distance between any numbers
            ans = min(ans, maxi)

        # we traverse in both directions at the same time, so we give half of the answer
        return (ans + 1) // 2