class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = Counter(s)
        seen = set()
        for i,char in enumerate(s):
            while stack and  char < stack[-1] and counter[stack[-1]] > 1 and char not in seen:
                cur_char = stack.pop()
                counter[cur_char] -= 1
                seen.remove(cur_char)
                
            if char not in seen: 
                stack.append(char)
                seen.add(char)
            else:
                counter[char] -= 1
                
        return "".join(stack)