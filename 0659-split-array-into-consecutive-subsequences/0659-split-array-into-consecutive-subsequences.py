class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1
        
        heap = []
        
        for k,v in hashMap.items():
            heapq.heappush(heap,k)
        
        while heap:
            minn = heap[0]
            count = 0
            while True:
                if minn not in hashMap:
                    if count < 3:
                        return False
                    break
                hashMap[minn] -= 1
                count += 1
                if hashMap[minn] == 0:
                    if minn != heap[0]:
                        return False
                    heapq.heappop(heap)
                if minn + 1 in hashMap and (hashMap[minn] >= hashMap[minn+1]):
                    if count < 3:
                        return False
                    break
                minn += 1
        return True