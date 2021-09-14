class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # word1 and word2 can be rename short_str and long_str according to their length
        # this question is a LCS problem
        # the answer should be len(word1) + len(word2) - 2 * len(LCS)
        
        m , n = len(word1) , len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        LCS_len = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                
                LCS_len = max(LCS_len , dp[i][j])

        return m + n - 2 * LCS_len
        
        

