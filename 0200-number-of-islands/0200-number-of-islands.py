class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(row, col):
            if not inbound(row, col) or visited[row][col] or grid[row][col] == "0":
                return
            
            visited[row][col] = True
            for r, c in directions:
                new_row = row + r
                new_col = col + c
                dfs(new_row, new_col)
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    count += 1
                    dfs(i, j)
                    
        return count