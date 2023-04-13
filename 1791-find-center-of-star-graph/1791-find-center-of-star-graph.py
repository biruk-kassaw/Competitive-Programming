class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        star = set()
        for i,j in edges:
            if i in star:
                return i
            if j in star:
                return j
            star.add(i)
            star.add(j)