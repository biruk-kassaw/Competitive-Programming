class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(idx, arr):
           
            if len(arr) == k:
                ans.append(list(arr))
                return
            
            for i in range(idx,n+1):
                arr.append(i)
                backtrack(i+1, arr)
                arr.pop()            
            
        backtrack(1,[])
        return ans