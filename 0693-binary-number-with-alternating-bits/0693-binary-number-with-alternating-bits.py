class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        isOn = n & 1
        n >>= 1
        
        while n > 0:
            last = n & 1
            if isOn:
                if last:
                    return False
                else:
                    isOn = False
            else:
                if last:
                    isOn = True
                else:
                    return False
            n >>= 1
        return True