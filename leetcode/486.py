class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # dp[i][j] means highest score player 1 can get from initial array nums[i:j+1]
        # dp[i][j] = max(nums[i] + sum(nums[i+1:j+1]) - dp[i+1][j], nums[j] + sum(nums[i:j]) - dp[i][j-1])
        dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]

        def cal_score(i , j):
            if dp[i][j] != -1:
                return dp[i][j]
            if i == j:
                dp[i][j] = nums[i]
                return dp[i][j]

            choose_left = nums[i] + sum(nums[i+1:j+1]) - cal_score(i+1, j)
            choose_right = nums[j] + sum(nums[i:j]) - cal_score(i,j-1)
            dp[i][j] = max(choose_left,choose_right)
            return dp[i][j]

        if sum(nums) % 2 == 0 and cal_score(0,len(nums)-1) >= sum(nums) // 2:
            return True
        elif sum(nums) % 2 != 0 and cal_score(0,len(nums)-1) >= sum(nums) // 2 + 1:
            return True
        else:
            return False