class Stack:
    def __init__(self):
        self.s=[]
        
    def push(self,val):
        self.s.append(val)
        
    def pop(self):
        return self.s.pop()
    
    def isEmpty(self):
        return self.s==[]

class MyQueue:

    def __init__(self):
        self.ip=Stack()#inputStack
        self.op=Stack()#outputStack

    def push(self, x: int) -> None:
        self.ip.push(x)
            
    
    def pop(self) -> int:
        if self.op.isEmpty():
            while self.ip.s:
                self.op.push(self.ip.pop())
            return self.op.pop()
        else:
            return self.op.pop()

    def peek(self) -> int:
        if self.op.isEmpty():
            while self.ip.s:
                self.op.push(self.ip.pop())
            return self.op.s[-1]
        else:
            return self.op.s[-1]
            

    def empty(self) -> bool:
        return self.ip.isEmpty() and self.op.isEmpty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
