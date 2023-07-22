class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dfs(i):
            if i >= len(questions):
                return 0
            return max(dfs(i+1), questions[i][0] + dfs(questions[i][1]+1+i))
        return dfs(0)