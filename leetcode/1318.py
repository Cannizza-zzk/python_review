class Solution:
    def to_bi(self, a:int)->str:
        ans = ['0'] * 32
        i = 1
        while a != 0:
            ans[-i] = str(a%2)
            a//=2
            i += 1
        #ans.reverse()
        return ''.join(ans)

    def minFlips(self, a: int, b: int, c: int) -> int:
        binC = self.to_bi(c)
        binAandB = self.to_bi(a&b)
        bitFlag = self.to_bi((a | b) ^ c)
        ans = 0
        for i in range(len(bitFlag)):
            if bitFlag[i] == '1':
                if binC[i] == '0':
                    if binAandB[i] == '0':
                        ans += 1
                    else:
                        ans += 2
                else:
                    ans += 1
        return ans
