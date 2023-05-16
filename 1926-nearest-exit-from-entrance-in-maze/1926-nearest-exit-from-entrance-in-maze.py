class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque([tuple(entrance)])
        steps = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur != tuple(entrance) and (0 == cur[0] or  cur[0] == len(maze)-1 or cur[1] == len(maze[0])-1 or cur[1] == 0):
                    return steps
                for dx, dy in directions:
    
                    new_row = cur[0] + dx
                    new_col = cur[1] + dy
                    if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == ".":
                        maze[new_row][new_col] = "+"
                        q.append((new_row, new_col))
            steps += 1
        return -1