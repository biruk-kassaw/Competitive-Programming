class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        for a, b in prerequisites:
            graph[b].add(a)
        
        preqMap = {}
        def dfs(course):
            if course not in preqMap:
                cur = set()
                for child in graph[course]:
                    cur |= dfs(child)
                    
                cur.add(course)
                preqMap[course] = cur
                
            return preqMap[course]
        
        for i in range(numCourses):
            dfs(i)
            
        res = []
        for a, b in queries:
            res.append(a in preqMap[b])
        return res
