import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = maxchar = 0
        charcnt = collections.Counter()
        res = 0
        for j in range(len(s)):
            charcnt[s[j]] += 1
            maxchar = max(charcnt[s[j]], maxchar)
            
            if j - i + 1 > maxchar + k:
                charcnt[s[i]] -= 1
                i += 1
            res = max(j-i+1, res)

        return res

# reference: https://leetcode.com/problems/longest-repeating-character-replacement/discuss/278271/JavaC%2B%2BPython-Sliding-Window-just-O(n)