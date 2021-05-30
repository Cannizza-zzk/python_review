class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m , n = len(grid) , len(grid[0])
        dpl2r = grid.copy()
        dpr2l = grid.copy()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i - 1 >= 0 and j - 1 >= 0:
                    dpl2r[i][j] += dpl2r[i-1][j-1]
                if i - 1 >= 0 and j + 1 < len(grid[0]):
                    dpr2l[i][j] += dpr2l[i-1][j+1]
        maxL = min(m,n) // 2
        ans = []
        for L in range(1,maxL+1):
            for i in range(m):
                for j in range(n):
                    if i + L - 1 < m and i - L + 1 >= 0 and j + L - 1 < n and j - L + 1 >= 0:
                        res = 0
                        res += dpl2r[i][j+L-1] - dpl2r[i-L+1-1][j-1] if i-L >=0 and j - 1 >= 0 else dpl2r[i][j+L-1]
                        res += dpl2r[i+L-1][j] - dpl2r[i-1][j-L+1 -1] if i - 1 >= 0 and j - L >= 0 else dpl2r[i+L-1][j]
                        res += dpr2l[i+L-1][j] - dpr2l[i-1][j+L-1+1] if i - 1 >= 0 and j+ L < n else dpr2l[i+L-1][j]
                        res += dpr2l[i][j-L+1] - dpr2l[i-L+1-1][j+1] if i - L >= 0 and j + 1 < n else dpr2l[i][j-L+1]
                        if len(ans) < 3:
                            ans.append(res)
                            ans.sort(reverse=True)
                        elif res > ans[2]:
                            ans[2] = res
                            ans.sort(reverse=True)
        
        return ans
