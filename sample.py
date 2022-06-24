class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        mine = 0
        while piles != []:
            alice = piles.pop()
            mine += piles.pop()
            bob = piles.pop(0)
        return mine
