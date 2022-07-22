class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        z_pos = {'r':[],'c':[]}
        m, n  = len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    z_pos['c'].append(j)
                    z_pos['r'].append(i)
        for r in z_pos['r']:
            matrix[r][:] = [0]*m
        for c in z_pos['c']:
            for i in range(m):
                matrix[i][c] = 0

        return

# O(1) space solution: https://leetcode.com/problems/set-matrix-zeroes/discuss/26014/Any-shorter-O(1)-space-solution