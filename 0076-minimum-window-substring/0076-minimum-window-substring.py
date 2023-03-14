class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        # if len(t) > len(s):
        #     return ""
        ans = [0,float("inf")]
        left = 0
        
        counter_t = Counter(t)
        counter_s = {}
        
        nedded = len(counter_t)
        found  = 0
        for i, char in enumerate(s):
            if char in t:
                counter_s[char] = counter_s.get(char, 0) + 1
                if counter_s[char] == counter_t[char]:
                    found += 1
                    
            while nedded == found:
                ans = [left, i] if i-left+1 < ans[1]-ans[0] + 1 else ans
                if s[left] in counter_t:
                    counter_s[s[left]] -= 1
                    if counter_s[s[left]] < counter_t[s[left]]:
                        found -= 1
                left += 1
        print(ans)
        return "" if ans[1] == float("inf") else s[ans[0]:ans[1]+1]