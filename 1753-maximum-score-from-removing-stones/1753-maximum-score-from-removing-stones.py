class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        maximum = max(a, b, c)
        minimum = min(a, b, c)
        middle = a + b + c - maximum - minimum

        if minimum + middle < maximum:
            return minimum + middle

        return (a + b + c) // 2