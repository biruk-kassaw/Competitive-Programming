class Solution:
    def countArrangement(self, n: int) -> int:
        count = [0]
        
        def backtrack(arr, visited):
            # print(arr)
            if len(arr) == n:                
                count[0] += 1
                return 
            
            for i in range(n):
                if i+1 not in visited and ((i+1) % (len(arr)+1) == 0 or ((len(arr)+1) % (i+1)==0) ):
                    arr.append(i+1)
                    visited.add(i+1)
                    backtrack(arr, visited)
                    arr.pop()
                    visited.remove(i+1)
                
            
        backtrack([],set())
        
        return count[0]