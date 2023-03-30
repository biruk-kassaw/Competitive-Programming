class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        next_n = n//2
        rem = n % 2
        while next_n > 0:
            if next_n % 2 == rem:
                return False
            rem = next_n % 2
            next_n = next_n//2
            
        return True