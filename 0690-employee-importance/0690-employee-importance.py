"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ans = [0]
        emap = {e.id: e for e in employees}
        def dfs(id):
            ans[0] += emap[id].importance
            for employee_id in emap[id].subordinates:
                dfs(employee_id)
        dfs(id)
        return ans[0]