class Solution:
    def is_palindrome(self,s:str):
        mid = len(s) // 2 if len(s) % 2 == 0 else len(s) // 2 + 1
        for i in range(mid):
            if s[i] != s[-i-1]:
                return False
        return True

    def removePalindromeSub(self, s: str) -> int:
        if self.is_palindrome(s):
            return 1
        else:
            return 2