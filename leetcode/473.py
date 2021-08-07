class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_len = sum(matchsticks)
        if total_len % 4 != 0:
            return False

        state = ''
        for i in range(len(matchsticks)):
            state += '1'
        dp = {}
        def dfs(state,targ,stage):
            if state in dp:
                return dp[state]

            if targ == 0:
                if stage == 3:
                    return True
                else:
                    stage += 1
                    targ += total_len // 4
            elif targ < 0:
                return False

            for i in range(len(matchsticks)):
                if state[i] == '1':
                    state_next = state[:i] + '0' + state[i+1:]
                    flag = dfs(state_next,targ-matchsticks[i],stage)
                    dp[state] = flag if state not in dp else dp[state] | flag
            return dp[state]
        
        return dfs(state, total_len//4, 0)


