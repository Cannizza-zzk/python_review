class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        ans  = {i : 1 for i in p}

        length = 1
        for char, char_next in zip(p,p[1:]):
            length = length + 1 if (ord(char_next) - ord(char)) % 26 == 1 else 1
            ans[char_next] = max(length, ans[char_next])

        return sum(ans.values())

# reference: https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95441/Python-Concise-Solution
# explanation:
#   1. ans[i] means the longest substring (can be find in wrapround string) ended with character i
#   2. ans[i] also means the number of substring ended with character i

