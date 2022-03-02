from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, j, d in edges:
            graph[i].append([j,d])
            graph[j].append([i,d])

        def dijstra():
            minheap = [(0, n)] # dist, node
            dist = [float('inf')] * (n + 1)
            dist[n] = 0

            while minheap:
                d, u = heappop(minheap)
                if d != dist[u]: continue
                for v, dis_uv in graph[u]:
                    if dist[v] > dist[u] + dis_uv:
                        dist[v] = dist[u] + dis_uv
                        heappush(minheap,(dist[v],v))
            return dist

        # dp[i] = sum(dp[j] | where j is adj of i and dist[j] < dist[i]) + 1 * (if i can reach last node)
        dist2n = dijstra()
        dp = [-1] * (n + 1)

        def find_dp(i):
            if dp[i] != -1:
                return dp[i]
            
            cnt = 0
            for next_n, _ in graph[i]:
                if next_n == n:
                    cnt += 1
                    continue
                
                if dist2n[i] > dist2n[next_n]:
                    cnt += find_dp(next_n)

            dp[i] = cnt % (1e9 + 7)

            return int(dp[i])

        return find_dp(1)

