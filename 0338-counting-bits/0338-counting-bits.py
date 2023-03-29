class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1,n+1):
            cur = i
            count = 0
            while cur > 0:
                cur_bit = cur & 1
                count += cur_bit
                cur = cur >> 1
            ans.append(count)
        return ans