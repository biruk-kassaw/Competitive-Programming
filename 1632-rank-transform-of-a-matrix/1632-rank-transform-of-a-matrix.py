class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = [[0 for j in range(n)] for i in range(m)]
        mp = defaultdict(list)
        for i in range(m):
            for j in range(n):
                mp[matrix[i][j]].append((i,j))
        fa, maxx, row, col = [0]*(m+n), [0]*m, [0]*m, [0]*n
        def getFa(x):
            if x != fa[x]: fa[x] = getFa(fa[x])
            return fa[x]
        for k, v in sorted(mp.items()):
            for (i, j) in v:
                fa[i] = fa[m+j] = i
                maxx[i] = 0
            for (i, j) in v:
                fa[getFa(m+j)] = getFa(i)
            for (i, j) in v:
                maxx[getFa(i)] = max(maxx[getFa(i)], row[i], col[j])
            for (i, j) in v:
                row[i] = col[j] = res[i][j] = maxx[getFa(i)] + 1
        return res