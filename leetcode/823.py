class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        sorted_arr = sorted(arr)
        dp = []
        for i in range(0,len(sorted_arr)):
            cnt = 1
            for j in range(0,i):
                if sorted_arr[i] % sorted_arr[j] == 0 and sorted_arr[i] / sorted_arr[j] in sorted_arr:
                    if sorted_arr[i] == sorted_arr[j]**2:
                        cnt += dp[j] ** 2
                    else:
                        index_ = sorted_arr.index(sorted_arr[i] / sorted_arr[j])
                        cnt += dp[j] * dp[index_]
            dp.append(cnt % mod)
    
        return sum(dp) % mod