class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                string = ""
                while stack[-1] != "[":
                    string = stack.pop() + string
                stack.pop()
                
                k = ""
                
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                if string != "":
                    stack.append(int(k) * string)
        while stack and stack[-1].isdigit():
            stack.pop()
        return "".join(stack)