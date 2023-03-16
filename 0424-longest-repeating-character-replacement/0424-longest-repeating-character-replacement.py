class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = Counter()
        ans = 0
        left = 0
        
        for i, char in enumerate(s):
            
            seen[char] += 1
            
            while (i-left +1) - max(seen.values()) > k:
                seen[s[left]] -= 1
                left += 1
            ans = max(ans, i-left+1)
            
        return ans