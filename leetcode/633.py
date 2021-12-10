class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left_ptr , right_ptr = 0 , int(c**0.5)
        while left_ptr <= right_ptr:
            cur = left_ptr**2 + right_ptr**2
            if c == cur:
                return True
            elif c > cur:
                left_ptr += 1
            else:
                right_ptr -= 1

        return False