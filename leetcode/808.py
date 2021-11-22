class Solution:
    def soupServings(self, n: int) -> float:
        # dp[(m,n)] means possiblity when initial state is m ml A & n ml B
        # dp[(m,n)] = 0.25 * (dp[(m-100,n)] + dp[(m-75,n-25)] + dp[(m-25,n-75)] + dp[(m-50, n-50)])

        dp = {}
        dm , dn = [100, 75, 50, 25], [0, 25, 50, 75]
        if n > 4800:
            return 1

        def get_prob(m, n):
            if m <= 0 and n > 0 :
                dp[(m,n)] = 1
            elif m <= 0 and n <= 0:
                dp[(m,n)] = 0.5
            elif m > 0 and n <= 0:
                dp[(m,n)] = 0

            if (m,n) in dp:
                return dp[(m,n)]

            dp[(m,n)] = 0
            for i in range(4):
                dp[(m,n)] += 0.25 * get_prob(m-dm[i],n-dn[i])

            return dp[(m,n)]

        return get_prob(n,n)

# reference: https://leetcode.com/problems/soup-servings/discuss/121711/C%2B%2BJavaPython-When-N-greater-4800-just-return-1
# lee215 yyds