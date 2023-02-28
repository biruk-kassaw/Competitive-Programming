class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.prefix = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for row in range(1,len(matrix)+1):
            for col in range(1,len(matrix[0])+1):
                
                self.prefix[row][col]+=self.prefix[row-1][col]+self.prefix[row][col-1]-self.prefix[row-1][col-1]+self.matrix[row-1][col-1]
                
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:    
        return self.prefix[row2+1][col2+1]-self.prefix[row1][col2+1]-self.prefix[row2+1][col1]+self.prefix[row1][col1]
        
