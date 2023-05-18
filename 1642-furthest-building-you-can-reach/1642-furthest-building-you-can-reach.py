class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        i = 0

        while i < len(heights)-1:
            
            if heights[i+1] > heights[i]:
                heappush(heap, heights[i+1] - heights[i])
                
                if len(heap) > ladders:
                    least = heappop(heap)
                    
                    if bricks < least:
                        break
                    bricks -= least
            i += 1

        return i
        
        
            
            
            