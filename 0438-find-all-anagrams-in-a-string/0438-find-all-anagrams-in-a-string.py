class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter_p = [0]*26
        for char in p:
            counter_p[ord(char) - ord("a")] += 1
        left = 0
        
        ans = []
        
        counter_s = [0] * 26
        for i in range(len(s)):
            counter_s[ord(s[i]) - ord("a")] += 1
            if i >= len(p) -1:
                if counter_p == counter_s:
                    ans.append(left)
                counter_s[ord(s[left]) - ord("a")] -= 1
                left += 1
                
        return ans
    
    