from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_course = defaultdict(list)
        degree = [0] * numCourses
        for i , j in prerequisites:
            degree[i] += 1
            pre_course[j].append(i)

        course_stack = []
        for i in range(numCourses):
            if degree[i] == 0:
                course_stack.append(i)

        ans = []
        while course_stack:
            c = course_stack.pop()
            ans.append(c)
            for j in pre_course[c]:
                degree[j] -= 1
                if degree[j] == 0:
                    course_stack.append(j)

        if len(ans) == numCourses:
            return ans
        else:
            return []