class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        ans = []
        for num in nums1:
            if num not in next_greater:
                ans.append(-1)
            else:
                ans.append(next_greater[num])
        return ans