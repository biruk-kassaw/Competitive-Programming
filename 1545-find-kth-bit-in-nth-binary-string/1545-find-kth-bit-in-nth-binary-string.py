class Solution:
    def length(self, n):
        if n == 1:
            return 1
        return 2*self.length(n-1) + 1 
    
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n,k):
            if n == 1:
                return "0"
            
            length = self.length(n)
            # print(length, k, n)
            
            if length // 2 >= k:
                return helper(n-1, k)
            else:
                if (length // 2) + 1 == k:
                    return "1"
                else:
                    offset = k - ((length//2) + 1)
                    k = (length//2) + 1 - offset
                    return str(1 -int(helper(n-1, k)))
        return helper(n,k)
