class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(row, col):
            
            if not inbound(row, col) or grid[row][col] == 0:
                return 1
            if grid[row][col] == 2: 
                return 0
            grid[row][col] = 2
            result = 0
            for r, c in directions:
                new_row = row + r
                new_col = col + c
                result += dfs(new_row, new_col)
            return result 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0 