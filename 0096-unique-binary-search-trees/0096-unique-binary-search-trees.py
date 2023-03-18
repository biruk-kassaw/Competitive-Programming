class Solution:
    def numTrees(self, n: int) -> int:
        cache = {}  
        
        def dp(start: int, end: int) -> int:
            if end <= start:  
                return 1      
            elif (start, end) in cache.keys():
                return cache[(start, end)]  
            result = 0
            for i in range(end-start+1):          
                result += dp(start, start+i-1) * dp(start+i+1, end)      
            cache[(start, end)] = result  
            return result
        
        return dp(1, n) 