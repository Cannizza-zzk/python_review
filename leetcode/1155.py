class Solution:
    def __init__(self) -> None:
        self.mod = 10**9 + 7
        self.dp ={}
    
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if (d, target) in self.dp:
            return self.dp[(d,target)]
        elif d == 0:
            self.dp[(d,target)] = 0 if target > 0 else 1
            return self.dp[(d,target)] 
        else:
            ans = 0
            for i in range(max(0,target -f),target):
                ans += self.numRollsToTarget(d - 1,f,i)
            self.dp[(d,target)] = ans
        
        return ans % self.mod