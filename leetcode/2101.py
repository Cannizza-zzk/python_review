from cmath import sqrt
from collections import defaultdict
from inspect import stack


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def distance(b1,b2):
            dx = b1[0] - b2[0]
            dy = b1[1] - b2[1]
            return math.pow(dx**2 + dy**2,0.5)

        dist_map = [[0 for _ in range(len(bombs))] for _ in range(len(bombs))]
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                dist_ij = distance(bombs[i], bombs[j])
                dist_map[i][j] = dist_ij
                dist_map[j][i] = dist_ij

        bomb_adj = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if j != i and bombs[i][2] >= dist_map[i][j]:
                    bomb_adj[i].append(j)

        ans = 0
        for i in range(len(bombs)):
            stack, cnt = [i], 0
            bomb_flag = [False]*len(bombs)
            bomb_flag[i] = True
            while stack:
                deto_bomb = stack.pop()
                cnt += 1
                for adj_bomb in bomb_adj[deto_bomb]:
                    if not bomb_flag[adj_bomb]:
                        stack.append(adj_bomb)
                        bomb_flag[adj_bomb] = True

            ans = max(ans,cnt)

        return ans


    