class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        num = image[sr][sc]
        
        def inbound(sr, sc):
            return 0 <= sr < len(image) and 0 <= sc < len(image[0])
        
        def dfs(sr, sc):
            if image[sr][sc] == color: return
            
            if image[sr][sc] != num:
                return
            
            
            
            image[sr][sc] = color
            for d_row, d_col in directions:
                new_row = sr + d_row
                new_col = sc + d_col
                if inbound(new_row, new_col):
                    dfs(new_row, new_col)
        
        dfs(sr, sc)
        return image