class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) == 0:
            return s2 == s3
        elif len(s2) == 0:
            return s1 == s3

        dp = [[-1 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        def dfs(p1,p2,p3) -> bool:
            if dp[p1+1][p2+1] != -1:
                return dp[p1 + 1][p2 + 1]
            if p1 >=0 and p2>=0:
                if s1[p1] == s3[p3] and s2[p2] == s3[p3]:
                    dp[p1+1][p2+1] =  dfs(p1-1,p2,p3-1) or dfs(p1,p2-1,p3-1)
                elif s1[p1] == s3[p3]:
                    dp[p1+1][p2+1] =  dfs(p1-1,p2,p3-1)
                elif s2[p2] == s3[p3]:
                    dp[p1+1][p2+1] =  dfs(p1,p2-1,p3-1)
                else:
                    dp[p1+1][p2+1] = False
                
            elif p1 >= 0:
                if dp[p1+1][p2+1] != -1:
                    return dp[p1][0]
                if s1[:p1+1] == s3[:p3+1]:
                    dp[p1+1][p2+1] = True
                else:
                    dp[p1+1][p2+1] = False
                return dp[p1+1][p2+1]
            elif p2 >= 0:
                if dp[p1+1][p2+1] != -1:
                    return dp[p1+1][p2+1]
                if s2[:p2+1] == s3[:p3+1]:
                    dp[p1+1][p2+1] = True
                else:
                    dp[p1+1][p2+1] = False
                
            return dp[p1+1][p2+1]

        return dfs(len(s1)-1,len(s2)-1,len(s3)-1)
