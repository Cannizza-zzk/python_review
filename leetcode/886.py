from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_p = defaultdict(list)
        for i , j in dislikes:
            adj_p[i-1].append(j-1)
            adj_p[j-1].append(i-1)

        visited = [0] * n
        visited[0] = 1
        p_stack = [0]

        while p_stack or 0 in visited:
            if not p_stack:
                next = visited.index(0)
                visited[next] = 1
                p_stack.append(next)
            pt = p_stack.pop()
            
            for p in adj_p[pt]:
                if visited[p] == 0:
                    visited[p] = -1 * visited[pt]
                    p_stack.append(p)
                elif visited[p] == visited[pt]:
                    return False

        return True


            