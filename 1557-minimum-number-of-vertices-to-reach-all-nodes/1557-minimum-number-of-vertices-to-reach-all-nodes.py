class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        froms = set()
        tos = set()
        
        for i,j in edges:
            froms.add(i)
            tos.add(j)
        ans = []
        for num in froms:
            if num not in tos:
                ans.append(num)
        return ans