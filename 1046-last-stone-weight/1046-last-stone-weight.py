class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while stones:
            first = -heapq.heappop(stones)
            if not stones:
                return first
            second = -heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, -(first - second))
                
        return 0