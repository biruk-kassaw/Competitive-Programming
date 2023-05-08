class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incomings = [0]*numCourses
        q = deque()
        
        for a,b in prerequisites:
            graph[b].append(a)
            incomings[a] += 1
        for i in range(numCourses):
            if incomings[i] == 0:
                q.append(i)
        ans = []    
        while q:
            cur = q.pop()
            ans.append(cur)
            for child in graph[cur]:
                incomings[child] -= 1
                if incomings[child] == 0:
                    q.append(child)
                    
        return ans if len(ans) == numCourses else []