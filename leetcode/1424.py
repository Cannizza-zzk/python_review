class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        rcd =  []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                row_idx = i + j
                if len(rcd) == row_idx:
                    rcd.append([])
                rcd[row_idx].insert(0, nums[i][j])

        res = []
        for row in rcd:
            for ele in row:
                res.append(ele)
        return res