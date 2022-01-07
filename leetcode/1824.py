
def minSideJumps(self, A):
        dp = [1, 0, 1]
        for a in A:
            if a:
                dp[a - 1] = float('inf')
            for i in range(3):
                if a != i + 1:
                    dp[i] = min(dp[i], dp[(i + 1) % 3] + 1, dp[(i + 2) % 3] + 1)
        return min(dp)



# reference: https://leetcode.com/problems/minimum-sideway-jumps/discuss/1152665/JavaC%2B%2BPython-DP-O(1)-space






""" 
TLE

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        # dp[i][lane] = slide_jumps
        # slide jumps means min num of slide jumps needed to get i
        # lane means position at point i
        # dp[i][lane] = min(dp[i-1][lane], dp[i-1][other_lane] + 1)
        n = len(obstacles)
        dp = [[float('inf') for _ in range(4)] for _ in range(n)]

        dp[0] = [0, 1, 0, 1]

        for i in range(1 , n):
            obstacle = obstacles[i]
            pre_obstale = obstacles[i-1]
            for j in range(1, 4):
                for k in range(1, 4):
                    if k == pre_obstale or k == obstacle:
                        continue
                    dp[i][j] = min(dp[i-1][j],dp[i-1][k]+1, dp[i][j])

            
            dp[i][obstacle] = float('inf')
        #print(dp)
        return min(dp[n-1])
 """