class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        
        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        def getSurrounding(row, col):
            val = 0
            for r, c in directions:
                new_row = row + r
                new_col = col + c
                if inbound(new_row, new_col) and board[new_row][new_col] == "M":
                    val += 1
            return val
        
        def dfs(row, col):
            if board[row][col] == "M":
                board[row][col] = "X"
                return
            if board[row][col] == "E":
                val = getSurrounding(row, col)
                if val:
                    board[row][col] = str(val)
                else:
                    board[row][col] = "B"
                    for r, c in directions:
                        new_row = row + r
                        new_col = col + c
                        if inbound(new_row, new_col) and board[new_row][new_col] != "B":
                            dfs(new_row, new_col)
        
        dfs(click[0], click[1])
        return board