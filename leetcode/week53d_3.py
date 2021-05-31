class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m , n = len(grid) , len(grid[0])
        dpl2r = [i.copy() for i in grid]
        dpr2l = [i.copy() for i in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i - 1 >= 0 and j - 1 >= 0:
                    dpl2r[i][j] += dpl2r[i-1][j-1]
                if i - 1 >= 0 and j + 1 < len(grid[0]):
                    dpr2l[i][j] += dpr2l[i-1][j+1]
        if min(m,n) % 2 == 0:
            maxL = min(m,n) // 2
        else:
            maxL = min(m,n) // 2 + 1
        ans = []
        #print(dpl2r)
        #print(dpr2l)
        for L in range(1,maxL+1):
            #print(L)
            for i in range(m):
                for j in range(n):
                    if i + L - 1 < m and i - L + 1 >= 0 and j + L - 1 < n and j - L + 1 >= 0:
                        res = 0
                        res += dpl2r[i][j+L-1] - dpl2r[i-L+1-1][j-1] if i-L >=0 and j - 1 >= 0 else dpl2r[i][j+L-1]
                        res += dpl2r[i+L-1][j] - dpl2r[i-1][j-L+1 -1] if i - 1 >= 0 and j - L >= 0 else dpl2r[i+L-1][j]
                        res += dpr2l[i+L-1][j] - dpr2l[i-1][j+L-1+1] if i - 1 >= 0 and j+ L < n else dpr2l[i+L-1][j]
                        res += dpr2l[i][j-L+1] - dpr2l[i-L+1-1][j+1] if i - L >= 0 and j + 1 < n else dpr2l[i][j-L+1]
                        
                        if L == 1:
                            res //= 4
                        else:
                            res -= (grid[i + L -1][j] + grid[i-L+1][j] + grid[i][j+L-1] + grid[i][j-L+1])
                        #print(i,j,L,res)
                        if len(ans) < 3:
                            ans.append(res)
                            ans.sort(reverse=True)
                            ans = list(set(ans))
                        elif res > ans[2]:
                            ans.append(res)
                            ans.sort(reverse=True)
                            ans = list(set(ans))
                            if len(ans) > 3:
                                ans.pop()
        
        return ans

        # 暴力解答 时间复杂度会在n^3内 没de完bug