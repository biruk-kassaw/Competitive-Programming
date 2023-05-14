class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = "#"
        for row, col in q:
            for dr, dc in (1,0), (-1,0), (0,1), (0,-1):
                new_row = dr + row
                new_col = dc + col
                
                if 0 <= new_row < len(mat) and 0 <= new_col < len(mat[0]) and mat[new_row][new_col] == "#":
                    mat[new_row][new_col] = mat[row][col] + 1
                    q.append((new_row, new_col))
        return mat