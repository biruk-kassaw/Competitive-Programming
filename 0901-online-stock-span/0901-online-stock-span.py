class StockSpanner:

    def __init__(self):
        self.stack = [] 

    def next(self, price: int) -> int:
        val = [price,1]
        while self.stack and self.stack[-1][0] <= price:
            cur = self.stack.pop()
            val[1] += cur[1]
        self.stack.append(val)
        return val[1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)