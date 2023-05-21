class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree = [0]*n
        res = [set() for _ in range(n)]

        for i in edges:
            graph[i[0]].append(i[1])
            in_degree[i[1]] += 1

        que = deque()
        for i in range(len(in_degree)):
            if not in_degree[i]:
                que.append(i)


        while que:
            node = que.popleft()

            for i in graph[node]:
                in_degree[i] -= 1
                res[i].add(node)

                for j in res[node]:
                    res[i].add(j)
                if not in_degree[i]:
                    que.append(i)

        for i in range(len(res)):
            res[i] = sorted(res[i])

        return res