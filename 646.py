class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # dp[i] means length of longest chain ended with pairs[i]
        # dp[i] = max(dp[k]| where k < i and pairs[k][1] < pairs[i][0]) + 1
        pairs.sort(key=lambda x : x[0])
        dp = [1 for _ in range(len(pairs))]

        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)