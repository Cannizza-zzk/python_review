class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        ansList  = [[0 for i in range(n)] for i in range(m)]
        for rc in indices:
            row = rc[0]
            col = rc[1]
            for i in range(n):
                ansList[row][i] += 1
            for i in range(m):
                ansList[i][col] += 1

        flatAns = [i for array in ansList for i in array]
        #print(flatAns)
        cnt = 0
        for i in flatAns:
            if i % 2 == 1:
                cnt += 1

        return cnt
        
# 二维列表的声明尽量用循环 形如[[0]*n]*m 用来声明二维数组会发生错误
# 参考https://blog.csdn.net/m0_37362454/article/details/82151193

        