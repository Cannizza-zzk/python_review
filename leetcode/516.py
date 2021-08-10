class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j] means longest subseq in s[i:j+1]
        # s[i] == s[j]: dp[i][j] = dp[i+1][j-1]
        # s[i] != s[j]: dp[i][j] = max(dp[i+1][j],dp[i,j+1])
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]

        def find_subseq(i,j):
            if dp[i][j] != -1:
                return dp[i][j]

            if j == i:
                dp[i][j] = 1
                return dp[i][j]
            elif j < i:
                dp[i][j] = 0
                return dp[i][j]

            if s[i] == s[j]:
                dp[i][j] = find_subseq(i+1,j-1) + 2
            else:
                dp[i][j] = max(find_subseq(i+1,j),find_subseq(i,j-1))

            return dp[i][j]

        return find_subseq(0,len(s)-1)
