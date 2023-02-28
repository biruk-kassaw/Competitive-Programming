class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        s = ""
        path += "/"
        
        while i < len(path):
            if path[i] == "/":
                if s == "..":
                    if stack:
                        stack.pop()
                elif s == "" or s == ".":
                    pass
                else:
                    stack.append(s)
                s = ""

            else:
                s += path[i]
            i += 1
            
        return "/"+"/".join(stack)