class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(cur, path):
            path.append(cur)
            if cur == destination:
                paths.append(list(path))
                return
            for node in adjList[cur]:
                dfs(node, path)
                path.pop()
        adjList = defaultdict(list)
        for i, adj in enumerate(graph):
            adjList[i].extend(adj)
        source = 0
        destination = len(adjList) - 1
        paths = []
        
        dfs(0, [])
        
        return paths