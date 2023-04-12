class Solution:
    def minSteps(self, n: int) -> int:
        def is_prime(num):
            d = 2
            while d*d <= num:
                if num % d == 0:
                    return False
                d += 1
            return True
        
        def find_nearest_divisor(num):
            d = 2
            while d*d <= num:
                if num % d == 0:
                    return num // d
                d += 1
            
        def findKeys(num):
            if is_prime(num):
                return num
            nearest_divisor = find_nearest_divisor(num)
            return (num//nearest_divisor) + findKeys(nearest_divisor)
        if n == 1:
            return 0
        return findKeys(n)