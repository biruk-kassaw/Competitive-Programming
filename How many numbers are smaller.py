class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numssorted = sorted(nums)
        ordered = {}
        answer = []
        for i in range(len(nums)):
            if numssorted[i] not in ordered:
                ordered[numssorted[i]] = i
        for j in nums:
            answer.append(ordered[j])
        return answer
