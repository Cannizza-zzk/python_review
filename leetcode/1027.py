def longestArithSeqLength(self, A):
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())


# reference: https://leetcode.com/problems/longest-arithmetic-subsequence/discuss/274611/JavaC%2B%2BPython-DP

# DP solution TLE
""" class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # first two elements will ensure the whole sequence
        # traversal all possible (i,j) and record the seq length start with nums[i]&nums[j]
        res = 0
        if len(nums) < 2:
            return len(nums)
        
        dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
    
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                next_num = 2 * nums[j] - nums[i]
                if not next_num in nums[j+1:]:
                    dp[i][j] = 2
                else:
                    next_i, next_j = j , nums.index(next_num,min(j+1,len(nums)-1))
                    dp[i][j] = 1 + dp[next_i][next_j]
                res = max(dp[i][j],res)

        return res """
