class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == -2147483648 and divisor == -1): return 2147483647
        ans = 1
        nORp = 1 if (dividend > 0) == (divisor > 0) else -1
        a , b = abs(dividend) , abs(divisor)
        if a < b : return 0
        elif a == b: return ans * nORp
        while a > b:
            b <<= 1
            ans <<= 1
        ans >>= 1
        b >>= 1
        ans += self.divide(a - b, abs(divisor))
        return nORp * ans
