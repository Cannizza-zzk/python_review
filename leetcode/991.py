class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        if y <= x:
            return y - x
        else:
            if y % 2 == 0:
                return 1 + self.brokenCalc(x,y//2)
            else:
                return 2 + self.brokenCalc(x,(y+1)//2)
