class Solution:
    def racecar(self, target: int) -> int:
        
        q = deque([(0, 1)])
        
        seen = set()
        seen.add((0,1))
        
        steps = 0
        
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur[0] == target:
                    return steps

                A = (cur[0] + cur[1], cur[1]*2)

                if A not in seen:
                    q.append(A)
                    seen.add(A)

                R = (cur[0], - 1 if cur[1] >= 0 else 1)

                if R not in seen:
                    q.append(R)
                    seen.add(R)

            steps += 1
            
            
            