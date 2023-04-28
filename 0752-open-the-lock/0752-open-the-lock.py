class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def children(wheel):
            res = []
            for i in range(4):
                digit = str((int(wheel[i]) + 1) % 10)
                res.append(wheel[:i] + digit + wheel[i + 1 :])
                digit = str((int(wheel[i]) + 10 - 1) % 10)
                res.append(wheel[:i] + digit + wheel[i + 1 :])
            return res
        
        queue = deque()
        visited = set(deadends)
        
        if "0000" in visited:
            return -1
        
        queue.append(["0000", 0])
        while queue:
            wheel, turns = queue.popleft()
            if wheel == target:
                return turns
            
            for child in children(wheel):
                if child not in visited:
                    visited.add(child)
                    queue.append([child, turns + 1])
        return -1