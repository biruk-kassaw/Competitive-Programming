class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = "({["
        if len(s) == 1:
            return False
        for i in s:
            if i in openings:
                stack.append(i)
            elif stack == []:
                return False
            else:
                if i == ")" and stack.pop() == "(":
                    pass
                elif i == "}" and stack.pop() == "{":
                    pass
                elif i == "]" and stack.pop() == "[":
                    pass    
                else:
                    return False
        if stack != []:
            return False
        return True
