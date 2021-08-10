class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums_sum = sum(nums)
        pre_sum = [nums[0]]
        for i in range(1,len(nums)):
            pre_sum.append(pre_sum[-1]+nums[i])

        # dp[i,j] means number of expression can be form to target j using nums[0:i+1]
        
        dp = {}
        def expNum(i,j):
            nonlocal nums_sum
            if pre_sum[i] < j or pre_sum[i] < -1 * j:
                dp[(i,j)] = 0
                return dp[(i,j)]
            if (i,j) in dp:
                return dp[(i,j)]

            if i == 0:
                if j == nums[i] or j == -1 * nums[i]:
                    if nums[i] == 0:
                        dp[(i,j)] = 2
                    else:
                        dp[(i,j)] = 1
                else:
                    dp[(i,j)] = 0
                return dp[(i,j)]

            dp[(i,j)] = expNum(i-1, j - nums[i]) + expNum(i-1, j + nums[i])
            return dp[(i,j)]

        return expNum(len(nums)-1,target)




