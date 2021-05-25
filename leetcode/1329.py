class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for iters in range(len(mat)):
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if i + 1 < len(mat) and j + 1 < len(mat[0]) and mat[i][j] > mat[i+1][j+1]:
                        mat[i][j] , mat[i+1][j+1] = mat[i+1][j+1], mat[i][j]

        return mat