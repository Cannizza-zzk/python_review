class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # dp[i] means min clips for first i minutes
        # dp[i] = min(dp[i], dp[i - k] + 1 for every (i-k,i) in clips array)
        dp = [101] *  (101)
        dp[0], res = 0, 0

        for s , e in sorted(clips):
            for i in range(s, e+1):
                dp[i] = min(dp[i], dp[s] + 1)

        return -1 if dp[time] > 100 else dp[time]

# reference:https://leetcode.com/problems/video-stitching/discuss/270036/JavaC%2B%2BPython-Greedy-Solution-O(1)-Space
