class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = list(zip(scores, ages))
        players.sort(key=lambda x : x[0])
        players.sort(key=lambda x : x[1])

        # dp[i] means largest sum in players[:i+1] included i + 1
        # dp[i+1] = max(scores[i+1] + dp[j] where scores[j] < scores[i+1])
        # ans = max(dp)

        dp = [player[0] for player in players]

        for i in range(1,len(players)):
            for j in range(i):
                dp[i] = max(dp[j] + players[i][0],dp[i]) if players[i][0] >= players[j][0] else dp[i]

        return max(dp)