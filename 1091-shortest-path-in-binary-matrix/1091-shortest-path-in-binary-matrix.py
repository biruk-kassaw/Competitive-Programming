class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def inbound(row, col):
            return 0 <= row <  len(grid) and 0 <= col < len(grid[0])
        if grid[0][0] == 1:
            return -1
        
        visited = set()
        queue = deque([((0,0),1)])
        
        while queue:
            cur, distance = queue.popleft()
            
            if cur[0] == len(grid)-1 and cur[1] == len(grid)-1:
                return distance
            
            directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
            
            for row,col in directions:
                new_row = row + cur[0]
                new_col = col + cur[1]
                
                if inbound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 0:
                    queue.append(((new_row, new_col), distance + 1))
                    visited.add((new_row, new_col))
                    
        return -1