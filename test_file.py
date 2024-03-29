class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.occurence = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.occurence += 1
            if self.occurence >= self.k:
                return True
            else:
                return False
        else:
            self.occurence = 0
            return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
