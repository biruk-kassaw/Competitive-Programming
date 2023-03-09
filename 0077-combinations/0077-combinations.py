class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(idx, arr):
            if idx > n + 1:
                return
            
            if len(arr) == k:
                ans.append(list(arr))
                return
            
            arr.append(idx)
            backtrack(idx+1, arr)
            arr.pop()
            backtrack(idx+1, arr)
            
            
            
        backtrack(1,[])
        return ans