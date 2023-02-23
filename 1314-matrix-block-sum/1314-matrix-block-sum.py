class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefix = []
        row  = len(mat)
        col = len(mat[0])
        
        for r in range(row + 1):
            prefix.append([0 for c in range(col + 1)])
        
        for r in range(1,row + 1):
            for c in range(1, col + 1):
                prefix[r][c] = prefix[r-1][c] + prefix[r][c-1] + mat[r-1][c-1] - prefix[r-1][c-1]
        
        def sumRegion(row1,col1,row2,col2):
            return prefix[row2+1][col2+1] - prefix[row2+1][col1] - prefix[row1][col2 + 1] + prefix[row1][col1]
        
        res = []
        
        for r in range(row):
            curRow = []
            for c in range(col):
                r1 = r -k if r-k >=0 else 0
                r2 = r + k if r + k < row else row - 1
                c1 = c -k if c-k >= 0 else 0
                c2 = c + k  if c + k < col else col - 1
                curRow.append(sumRegion(r1,c1,r2,c2))
            res.append(curRow)
        return res