class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left <= right:
            mid = (left + right)//2
            total_hours = 0
            for pile in piles:
                if pile < mid:
                    total_hours += 1
                else:
                    total_hours += ((pile-1) // mid) + 1
            if total_hours > h:
                left = mid + 1
            else:
                right = mid-1
            
        return left
