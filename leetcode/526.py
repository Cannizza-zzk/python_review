class Solution:
    def countArrangement(self, n: int) -> int:
        state = '1' * n
        # dp[state] means number of targ arrangement 
        # easily dp[state] = sum(dp[possible_next_state])
        dp = {}
        dp['0'*n] = 1
        def dfs(state_now, index):
            # basic
            if state_now in dp:
                return dp[state_now]
            else:
                dp[state_now] = 0

            for i in range(len(state_now)):
                if state_now[i] == '1':
                    if (i + 1 > index and (i + 1) % index == 0) or (i + 1 < index and index % (i + 1) == 0) or index == i + 1:
                        next_state = state_now[0:i] + '0' + state_now[i+1:]
                        dp[state_now] += dfs(next_state, index+1)

            return dp[state_now]

        return dfs(state, 1)




        