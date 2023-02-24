class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_length = 0
        
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
                
            seen.add(s[i])
            max_length = max(max_length, len(seen))
            
        return max_length