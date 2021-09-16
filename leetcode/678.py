class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin , cmax = 0, 0
        for ch in s:
            cmax = cmax - 1 if ch == ')' else cmax + 1
            cmin = cmin + 1 if ch == '(' else max(cmin - 1, 0)
            if cmax < 0: return False
        if cmin != 0: return False
        else: return True
        
# reference: https://leetcode.com/problems/valid-parenthesis-string/discuss/107570/JavaC%2B%2BPython-One-Pass-Count-the-Open-Parenthesis
# lee215 yyds