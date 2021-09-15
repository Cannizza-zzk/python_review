class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[i][j] means if s[i:j+1] is a palindromic
        # dp[i][j] = dp[i+1][j-1] if s[i] == s[j] else 0
        # if j - i < 2 : dp[i][j] = 1 if s[i]==s[j] else 0
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n-1 , -1, -1):
            for j in range(i, n):
                if j - i < 2:
                    dp[i][j] = 1 if s[i] == s[j] else 0
                else:
                    dp[i][j] = dp[i+1][j-1] if s[i] == s[j] else 0

        ans = 0
        for item in dp:
            ans += sum(item)

        return ans
        


""" 
class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[i] means number of substring ended with s[i]
        
        def is_palindromic(i ,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1

            return True

        dp = [0 for _ in range(len(s))]
        char_dict = {}
        
        for index, char in enumerate(s):
            if char not in char_dict:
                char_dict[char] = [index]
            else:
                char_dict[char].append(index)

            for candidate in char_dict[char]:
                if is_palindromic(candidate, index):
                    dp[index] += 1

        
        return sum(dp)



            

 """