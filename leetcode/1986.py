class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        initial_state = int('0b'+'1'*n,2)
        dp = {}

        def find_dp(state):
            if state in dp:
                return dp[state]

            if state == 0:
                dp[state] = (1, 0)
            else:
                ans = (float('inf'), float('inf'))
                for i in range(n):
                    if state & (1<<i):
                        pieces, last = find_dp(state - (1 << i))
                        full = (last + tasks[i] > sessionTime)
                        ans = min(ans, (pieces + full, tasks[i] + (1-full)*last))
            dp[state] = ans

            return dp[state]

        return find_dp((1<<n)-1)[0]


# reference: https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/discuss/1431829/Python-dynamic-programming-on-subsets-explained
