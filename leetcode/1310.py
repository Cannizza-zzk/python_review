class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        dp = []
        ans = []
        dp.append(arr[0])
        for i in range(1,len(arr)):
            dp.append(arr[i] ^ dp[i-1])

        def xor(start,end):
            if start == 0:
                return dp[end]
            else:
                return dp[end] ^ dp[start-1]

        for i in range(0, len(queries)):
            ans.append(xor(queries[i][0],queries[i][1]))

        return ans
