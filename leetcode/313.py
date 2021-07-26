class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        cnt, ans = 1, [1]
        dp = [0 for _ in range(len(primes))]

        while cnt < n:
            next_ugly , min_index = -1 , -1
            for i in range(len(primes)):
                if primes[i] * ans[dp[i]] == ans[-1]:
                    dp[i] += 1
                if next_ugly == -1 or next_ugly > primes[i] * ans[dp[i]]:
                    min_index = i
                    next_ugly = primes[i] * ans[dp[i]]
            dp[min_index] += 1
            ans.append(next_ugly)
            cnt += 1
          
        return ans[-1]
