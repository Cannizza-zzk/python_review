class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1

        def is_palindrome(i,j):
            if j < i: 
                return True
            if dp[i][j] == 0:
                return False
            elif dp[i][j] == 1:
                return True
            
            if s[i] == s[j] and is_palindrome(i+1, j-1):
                dp[i][j] = 1
                return True
            else:
                dp[i][j] = 0
                return False

        start , end  = 0 , 0
        for i in range(len(s)):
            for j in range(i + (end - start),len(s)):
                if s[i] != s[j]: continue
                if is_palindrome(i,j) and j - i > end -start:
                    start , end = i , j
        return s[start:end+1]
        