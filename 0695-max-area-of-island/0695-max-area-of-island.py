class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        max_area = [0]
        visited = set()
        
        def dfs(row, col):
            if (not inbound(row, col) or grid[row][col] == 0 or (row, col) in visited):
                return 0
            visited.add((row, col))
                
            return 1 + dfs(row + 1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1 and (i, j) not in visited:
                    
                    count = dfs(i, j)
                    max_area[0]=max(max_area[0], count)
        return max_area[0]