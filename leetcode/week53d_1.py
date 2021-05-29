class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3: return 0
        ans  = 0
        for i in range(len(s) - 2):
            if len(collections.Counter(s[i:i+3])) == 3:
                ans += 1
        return ans