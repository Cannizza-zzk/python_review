class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        slist = s.split(' ')
        ans = []
        for i in range(0,k):
            ans.append(slist[i])
        return ' '.join(ans)