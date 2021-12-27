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
        # BFS
        queue = []
        for employee in employees:
            if employee.id == id:
                queue.append(employee)

        ans = 0
        while len(queue) != 0:
            cur_employee = queue.pop(0)
            ans += cur_employee.importance

            for id in cur_employee.subordinates:
                for employee in employees:
                    if employee.id == id:
                        queue.append(employee)
                        break
            
        return ans