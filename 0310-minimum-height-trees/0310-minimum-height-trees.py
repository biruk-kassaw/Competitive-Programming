class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n <= 2:
            return [i for i in range(n)]
        
        graph = defaultdict(set)
        incomings = [0] * n
        
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
            incomings[a] += 1
            incomings[b] += 1
            
        q = deque()
        for i, incoming in enumerate(incomings):
            if incoming == 1:
                q.append(i)
                
        visited = set()
        remaining = n
        while remaining > 2:

            for _ in range(len(q)):
                cur = q.popleft()
                remaining -= 1
                visited.add(cur)
                for child in graph[cur]:
                    if child not in visited:
                        incomings[child] -= 1
                        if incomings[child] == 1:
                            q.append(child)

        return q