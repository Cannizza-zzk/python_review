class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        lower , upper = 0 , 1
        if left == 0: return 0
        while lower <= right:
            if lower <= left and upper > right:
                return lower + self.rangeBitwiseAnd(left - lower, right - lower)
            lower = 1 if lower == 0 else lower * 2
            upper *= 2

        return 0