class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxi = values[0]
        ans = maxi
        for i in range(1,len(values)):
            ans = max(ans, maxi + values[i] - i)
            maxi = max(maxi, values[i] + i)
        return ans