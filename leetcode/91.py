class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] means num of decode ways in [0,i]
        # dp[i] = dp[i-1](not combine) + pd[i-2](combine)
        self.leading_zero = False if s[0] != '0' else True
        dp = [-1 for _ in range(len(s))]
        dp[0] = 1

        def decode_ways(n):
            if dp[n] != -1:
                return dp[n]
            
            if s[n] != '0':
                comb = int(s[n-1:n+1])
                if comb <= 26 and comb >= 10:
                    if n - 2 >= 0:
                        dp[n] = decode_ways(n-1) + decode_ways(n-2)
                    else:
                        dp[n] = 2
                else:
                    dp[n] = decode_ways(n-1)
            else:
                comb = int(s[n-1:n+1])
                if comb > 20 or comb < 10:
                    self.leading_zero = True
                elif n-2 >= 0:
                    dp[n] = decode_ways(n-2)
                else:
                    dp[n] = decode_ways(n-1)

            return dp[n]
        decode_ways(len(s) -1)
        if self.leading_zero == True:
            return 0
        else:
            return dp[-1]
                