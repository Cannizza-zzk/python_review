from cmath import inf
from heapq import heappop, heappush


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append([v, t])
            graph[v].append([u, t])

        def dijstra():
            dist = [math.inf] * n
            way_cnt = [0] * n
            minheap = [(0, 0)] # distance , index
            dist[0] = 0
            way_cnt[0] = 1

            while minheap:
                d, idx = heappop(minheap)
                if dist[idx] < d : 
                    continue
                for v, t in graph[idx]:
                    if dist[v] > d + t:
                        dist[v] = d + t
                        way_cnt[v] = way_cnt[idx]
                        heappush(minheap,(dist[v],v))
                    elif dist[v] == d + t:
                        way_cnt[v] = (way_cnt[v] + way_cnt[idx]) % (1e9+7)
            return int(way_cnt[n-1])

        return dijstra()