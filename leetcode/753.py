class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            ans = range(k)
            ans = ''.join(map(str,ans))
            return ans
        path = '0' * (n - 1)
        pw_rcd = set()
        for i in range(k ** n):
            window = path[-n+1:]
            for elem in range(k-1,-1,-1): #反向遍历是为了尽可能晚的返回起始点
                if window + str(elem) not in pw_rcd:
                    path += str(elem)
                    break
        
        return path

