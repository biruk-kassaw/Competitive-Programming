class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if k % 2 == 1:
            return self.kthGrammar(n-1, math.ceil(k/2))
        else:
            return 1 - self.kthGrammar(n-1, math.ceil(k/2))
        