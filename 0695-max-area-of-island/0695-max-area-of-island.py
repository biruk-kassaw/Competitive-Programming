class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        max_area = [0]
        visited = set()
        
        def dfs(row, col):
                        
            visited.add((row, col))
            
            for dir_r, dir_c in directions:
                new_row = dir_r + row
                new_col = dir_c + col
                if not (not inbound(new_row, new_col) or grid[new_row][new_col] == 0 or (new_row, new_col) in visited):
                    dfs(new_row, new_col)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1 and (i, j) not in visited:
                    
                    count=len(visited)
                    dfs(i, j)
                    max_area[0]=max(max_area[0],len(visited)-count)
                    
        return max_area[0]