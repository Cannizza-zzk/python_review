class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        targ = [num+1, num+2]
        ans = [] # elem is like (divisor1, divisor2, dif)
        for elem in targ:
            divisor = int(pow(elem,0.5))
            while elem % divisor != 0:
                divisor -= 1
            ans.append((divisor,elem//divisor,abs(divisor - elem//divisor)))
        ans.sort(key=lambda x : x[2])
        return [ans[0][0],ans[0][1]]
            
        