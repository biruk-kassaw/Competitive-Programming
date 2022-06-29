class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = {}
        half_len = len(arr)//2
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        counted = sorted(count.values(), reverse=True)
        total_nums = 0
        total = 0
        for i in counted:
            if total < half_len:
                total += i
                total_nums += 1
        return total_nums
        
    
