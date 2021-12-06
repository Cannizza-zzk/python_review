class Solution:
    def sumSubarrayMins(self, A):
        n, mod = len(A), 10**9 + 7
        left, right, s1, s2 = [0] * n, [0] * n, [], []
        for i in range(n):
            count = 1
            while s1 and s1[-1][0] > A[i]: count += s1.pop()[1]
            left[i] = count
            s1.append([A[i], count])
        for i in range(n)[::-1]:
            count = 1
            while s2 and s2[-1][0] >= A[i]: count += s2.pop()[1]
            right[i] = count
            s2.append([A[i], count])
        return sum(a * l * r for a, l, r in zip(A, left, right)) % mod



# reference: https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/JavaC%2B%2BPython-Stack-Solution




# TLE solution
""" class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # dp[i][j] means min(arr[i:j+1])
        # dp[i][j] = min(dp[i][j-1], arr[j])

        dp = [0 for _ in range(len(arr))]
        res = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                dp[j] = arr[j] if j == i else min(dp[j-1], arr[j])
                res += dp[j]

        return res """