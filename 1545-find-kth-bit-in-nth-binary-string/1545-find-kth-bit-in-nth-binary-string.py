class Solution:
    def invert(self, n):
        new = []
        for i in range(len(n) - 1, -1, -1):
            char = n[i]
            if char == "1":
                new.append("0")
            else:
                new.append("1")
        return "".join(new)
    
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n):
            if n == 0:
                return "0"
            val = helper(n-1)
            return val + "1" + self.invert(val)
        res = helper(n)
        return res[k-1]
