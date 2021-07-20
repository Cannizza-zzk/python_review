class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row_size , col_size = len(rowSum) , len(colSum)
        res = [[0 for _ in range(col_size)] for _ in range(row_size)]
        for i in range(row_size):
            for j in range(col_size):
                res[i][j] = min(rowSum[i],colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]
        return res
        