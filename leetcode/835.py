from collections import defaultdict


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        N = len(img1)
        A, B = [], []
        for i in range(N):
            for j in range(N):
                if img1[i][j] == 1:
                    A.append(100*i + j)
                if img2[i][j] == 1:
                    B.append(100*i + j)
        if not A or not B: return 0
        cnt = defaultdict(int)
        for i in A:
            for j in B:
                cnt[i-j] += 1
        k = max(cnt,key=lambda x:cnt[x])
        return cnt[k]

# reference:https://leetcode.com/problems/image-overlap/discuss/130623/C%2B%2BJavaPython-Straight-Forward