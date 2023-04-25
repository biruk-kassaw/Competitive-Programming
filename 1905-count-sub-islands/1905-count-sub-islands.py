class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def inbound(row, col):
            return 0 <= row < len(grid2) and 0 <= col < len(grid2[0])
        
        def dfs(row, col):
            visited_l.add((row, col))
            visited.add((row, col))
            for dir_r, dir_c in directions:
                new_row = dir_r + row
                new_col = dir_c + col
                if inbound(new_row, new_col) and (new_row,new_col) not in visited and grid2[new_row][new_col] == 1:
                    dfs(new_row, new_col)
                    
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        count = 0
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i, j) not in visited:
                    visited_l  = set()
                    dfs(i, j)
                    is_sub = True
                    for row, col in visited_l:
                        if grid1[row][col] == 0:
                            is_sub = False
                    count += int(is_sub)
        return count