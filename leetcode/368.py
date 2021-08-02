class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        sorted_arr = sorted(nums)
        dp = [-1 for _ in range(len(sorted_arr))]
        dp[0] = 1
        for i in range(len(sorted_arr)):
            for j in range(i):
                if sorted_arr[i] % sorted_arr[j] == 0:
                    dp[i] = max(dp[j] + 1,dp[i])
                if  dp[i] == -1:
                    dp[i] = 1

        
        last = dp.index(max(dp))
        p, ans = last, [sorted_arr[last]]
        for i in range(last, -1, -1):
            if dp[i] == dp[p] - 1 and sorted_arr[p] % sorted_arr[i] == 0:
                ans.append(sorted_arr[i])
                p = i
        return ans