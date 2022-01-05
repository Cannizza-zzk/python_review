class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # dp[i][j] means max sum of arr[i:j+1]
        

        dp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]

        def get_dp(i,j):
            if dp[i][j] != 0:
                return dp[i][j]
            
            if i == j:
                dp[i][j] = arr[i]
            elif j - i + 1 <= k:
                dp[i][j] = max(arr[i:j+1]) * (j - i + 1)
            else:
                for p in range(k):
                    dp[i][j] = max(dp[i][j], get_dp(i,i+p) + get_dp(i+p+1,j))

            return dp[i][j]

        return get_dp(0,len(arr)-1)

""" 
reference: https://leetcode.com/problems/partition-array-for-maximum-sum/discuss/290863/JavaC%2B%2BPython-DP-O(K)-Space
def maxSumAfterPartitioning(self, A, K):
        N = len(A)
        dp = [0] * (N + 1)
        for i in xrange(1, N + 1):
            curMax = 0
            for k in xrange(1, min(K, i) + 1):
                curMax = max(curMax, A[i - k])
                dp[i] = max(dp[i], dp[i - k] + curMax * k)
        return dp[N] """