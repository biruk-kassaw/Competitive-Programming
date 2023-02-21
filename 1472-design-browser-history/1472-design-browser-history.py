class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        new_node.prev = self.cur
        self.cur.next = new_node
        self.cur = new_node
        

    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.cur.prev:
            self.cur = self.cur.prev
            i += 1
        return self.cur.val
    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.cur.next:
            self.cur = self.cur.next
            i += 1
        return self.cur.val
        
        
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)