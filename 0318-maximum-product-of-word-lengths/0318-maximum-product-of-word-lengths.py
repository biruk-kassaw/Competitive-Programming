class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_to_bit = {}
        
        for word in words:
            mask = 0
            for ch in word:
                pos = ord(ch)-ord('a')
                mask |= 1 << pos
            word_to_bit[word] = mask
        
        ans = 0
        
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if word_to_bit[words[i]] & word_to_bit[words[j]] == 0:
                    ans = max(ans, len(words[i])*len(words[j]))
        return ans