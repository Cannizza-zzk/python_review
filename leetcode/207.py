from collections import defaultdict
from email.policy import default


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_dict = defaultdict(list)
        for i, j in prerequisites:
            pre_dict[j].append(i)
        course_taken = [False for _ in range(numCourses)]

        while True:
            flag = False
            for i in range(numCourses):
                if len(pre_dict[i]) == 0 and not course_taken[i]:
                    course_taken[i] = True
                    flag = True
                    for j in range(numCourses):
                        if not course_taken[j] and i in pre_dict[j]:
                            pre_dict[j].remove(i) 
            if not flag:
                break
        if False in course_taken:
            return False
        else:
            return True





"""
BFS solution 
reference: https://leetcode.com/problems/course-schedule/discuss/162743/JavaC%2B%2BPython-BFS-Topological-Sorting-O(N-%2B-E)

def canFinish(self, n, prerequisites):
        G = [[] for i in range(n)]
        degree = [0] * n
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(n) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == n """