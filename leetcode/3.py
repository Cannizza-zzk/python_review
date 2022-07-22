class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        import collections
        p_rcd = collections.defaultdict(int)
        n, p1, p2 = len(s), 0, 0
        res = 0
        while p2 < n:
            p_rcd[s[p2]] += 1
        
            while p_rcd[s[p2]] > 1:
                p_rcd[s[p1]] -= 1
                p1 += 1
            
            res = max(res, p2 - p1 + 1)
            p2 += 1
        return res
                


        