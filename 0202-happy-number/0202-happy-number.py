class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            s = str(n)
            n = 0
            for digit in s:
                n += int(digit) ** 2
        return n == 1