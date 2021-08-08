class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i] means largest size of subset strs[:i]

        dp = {}
        

        def formSubset(i, m_remain, n_remain):
            if i == 0:
                return 0
            if (i,m_remain,n_remain) in dp:
                return dp[(i,m_remain,n_remain)]

            if strs[i-1].count('0') <= m_remain and strs[i-1].count('1') <= n_remain:
                dp[(i,m_remain,n_remain)] = max(formSubset(i-1,m_remain-strs[i-1].count('0'), n_remain-strs[i-1].count('1'))+1, formSubset(i-1,m_remain,n_remain))
            else:
                dp[(i,m_remain,n_remain)] = formSubset(i-1,m_remain,n_remain)

            return dp[(i,m_remain,n_remain)]

        return formSubset(len(strs),m,n)
