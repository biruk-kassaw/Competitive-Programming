class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        hashMap = {}
        q = deque()
        
        for i in range(len(nums2)):
            while q and nums2[i] > q[-1]:
                num = q.pop()
                hashMap[num] = nums2[i]
                
            q.append(nums2[i])
        while q:
            hashMap[q.pop()] = -1
        for i in nums1:
            ans.append(hashMap[i])
        return ans
