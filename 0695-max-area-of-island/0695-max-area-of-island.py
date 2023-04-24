class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        max_area = [0]
        visited = set()
        
        def dfs(count, row, col):
            if not inbound(row, col) or grid[row][col] == 0 or (row, col) in visited:
                return
            
            count += 1
            visited.add((row, col))
           
           
            for dir_r, dir_c in directions:
                new_row = dir_r + row
                new_col = dir_c + col
                
                dfs(count, new_row, new_col)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1 and (i, j) not in visited:
                    
                    count=len(visited)
                    dfs(0, i, j)
                    max_area[0]=max(max_area[0],len(visited)-count)
                    
        return max_area[0]