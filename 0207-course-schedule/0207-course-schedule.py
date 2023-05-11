class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        incomings = [0] * numCourses
        
        for a,b in prerequisites:
            graph[b].append(a)
            incomings[a] += 1
        
        q = deque()
        
        for i in range(numCourses):
            if  incomings[i] == 0:
                q.append(i)
        learned = 0
        while q:
            cur = q.popleft()
            learned += 1
            for child in graph[cur]:
                incomings[child] -= 1
                if incomings[child] == 0:
                    q.append(child)
                    
        return learned == numCourses