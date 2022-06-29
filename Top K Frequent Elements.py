class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        a = []
        for i in counter:
            a.append([i,counter[i]])
        a = sorted(a, key=lambda x: x[1], reverse=True)
        
        ans = []
        for i in range(k):
            ans.append(a[i][0])
        return ans
            
        
        
        
