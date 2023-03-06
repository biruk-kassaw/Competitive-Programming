class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.helper(x, n) 
        else:
            return 1/self.helper(x, -n)
        
    def helper(self, x, n): 
        if n == 0: #3
            return 1
        
        temp = self.myPow(x, n//2)
         
        if int(n%2) == 0:
            return  temp * temp
        else:
            return temp * temp * x 