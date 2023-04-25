class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def inbound(row, col):
            return 0 <= row < len(grid2) and 0 <= col < len(grid2[0])
        
        def dfs(row, col):
            if not inbound(row, col) or (row,col) in visited or grid2[row][col] == 0:
                return True
            
            visited.add((row, col))
            res =  True
            
            if grid1[row][col] != 1:
                res = False
                
            for dir_r, dir_c in directions:
                new_row = dir_r + row
                new_col = dir_c + col
#                 the order we call the function matters because and operator will shortcircuit if res is false
                res =  dfs(new_row, new_col) and res
                    
            return res
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        count = 0
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i, j) not in visited and dfs(i,j):
                    count += 1
                    
        return count