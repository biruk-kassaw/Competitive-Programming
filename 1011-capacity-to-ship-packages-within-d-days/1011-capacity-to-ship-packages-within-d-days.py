class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left+right) // 2
            day_count = 1
            total_weight = 0
            
            for weight in weights:
                total_weight += weight
                
                if total_weight > mid:
                    day_count += 1
                    total_weight = weight
            
            if day_count > days:
                left = mid + 1
            else:
                right = mid
        
        return left