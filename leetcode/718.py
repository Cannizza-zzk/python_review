class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j] means max length of common subarray which ended with nums1[i] & nums2[j]
        # in nums1[i] and nums2[j]
        # dp[i][j] = dp[i-1][j-1] + 1 if nums1[i] == nums2[j] else 0

        m , n = len(nums1) , len(nums2)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        maxLen = 0
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1 if i != 0 and j != 0 else 1
                maxLen = max(maxLen,dp[i][j])
        
        return maxLen