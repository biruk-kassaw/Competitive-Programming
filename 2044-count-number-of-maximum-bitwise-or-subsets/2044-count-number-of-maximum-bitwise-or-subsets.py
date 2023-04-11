class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_val = [0]
        max_val_count = [0]
        
        def backtrack(index, arr):
            if arr:
                local_or = 0
                
                for num in arr:
                    local_or |= num
                    
                if local_or == max_val[0]:
                    max_val_count[0] += 1
                elif local_or > max_val[0]:
                    max_val[0] = local_or
                    max_val_count[0] = 1
                    
            for i in range(index, len(nums)):
                arr.append(nums[i])
                backtrack(i + 1, arr)
                arr.pop()
                
        backtrack(0, [])
        return max_val_count[0]