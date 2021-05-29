class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m , n = len(grid) , len(grid[0])
        dpl2r = grid
        dpr2l = grid
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
                    if i + 2*(L-1) < m and j + L - 1 < n  and j - (L - 1) >= 0: # [i,j] [i + 2*(L-1),j] [i  + L-1 ,j -(L-1)] [i +L -1, j+L-1]
                        addres = 0
                        addres += dpl2r[i + L - 1][j + L - 1] - dpl2r[i][j]
                        addres += dpl2r[i+2*(L-1)][j] - dpl2r[i + L - 1][j - (L - 1)]
                        addres += dpr2l[i + (L -1)][j - (L - 1)] - dpr2l[i][j]
                        addres += dpr2l[i + 2*(L - 1)][j] - dpr2l[i+(L-1)][j+L-1]
                        if len(ans) < 3:
                            ans.append(addres)
                            ans.sort()
                        elif addres > ans[2]:
                            ans[2] = addres
                            ans.sort()
        
        return ans
