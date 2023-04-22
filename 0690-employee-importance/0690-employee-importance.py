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
        seen = set()
        def dfs(id):
            if id in seen:
                return
            for employee in employees:
                if employee.id == id:
                    ans[0] += employee.importance
                    seen.add(employee.id)

                    for employee_id in employee.subordinates:
                        dfs(employee_id)
                    break
        dfs(id)
        return ans[0]