class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res, cur = set(), set()
        for i in arr:
            cur = {i | j for j in cur} | {i}
            res |= cur
        return len(res)

# reference: https://leetcode.com/problems/bitwise-ors-of-subarrays/discuss/165881/C%2B%2BJavaPython-O(30N)


# memory limited solution
""" class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # dp[i][j] means result of arr[i:j+1]
        # dp[i][j] = dp[i][j-1] | arr[j]

        dp = [[-1 for _ in range(len(arr))] for _ in range(arr)]
        for i in range(len(arr)):
            dp[i][i] = arr[i]

        up_threshold, max_ele = 0, max(arr)

        for i in range(len(bin(max_ele)) - 2):
            up_threshold += 2**i

        res = set()
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                dp[i][j] = arr[j] | dp[i][j-1]
                res.add(dp[i][j])
                if dp[i][j] == up_threshold:
                    break

        if -1 in res:
            res.remove(-1)

        return len(res)
        

 """