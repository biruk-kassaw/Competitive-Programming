class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        if n > 12:
            return []
        def backtrack(s, arr):
            len_arr = sum([len(i) for i in arr])
            if len(arr) == 4 and len_arr == n:
                ans.append(list(arr))
                return
            
            if not s:
                return
            
            i = 1
            
            while i <= 3 and i <= len(s):
                cur = s[:i]
                if (cur == "0" or cur[0] != "0" ) and int(cur) < 256:
                    arr.append(cur)
                    backtrack(s[i:], arr)
                    arr.pop()
                i += 1
                
        backtrack(s, [])
        for i in range(len(ans)):
            ans[i] = ".".join(ans[i])    
        return ans
    
    
    
    
    
    
    
    