class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        upper_bound = 2**31
        n = len(num)
        for i in range(1, 11):
            for j in range(1, 11):
                if i + j > n: continue
                if (num[0] == '0' and i != 1) or (num[i] == '0' and j != 1): continue
                f1 , f2 = int(num[:i]), int(num[i:i+j])
                if f1 >= upper_bound or f2 >= upper_bound: continue
                targ , start = f1 + f2,  i + j
                path = [f1, f2]
                while start < n:
                    targ_len = len(str(targ))
                    if num[start] == '0' and targ_len != 1: break
                    if targ >= upper_bound: break
                    if start + targ_len <= n and targ == int(num[start:start + targ_len]):
                        path.append(targ)
                        f1, f2, targ = f2, targ, f2+targ
                        start = targ_len + start
                    else:
                        break
                if n == start and len(path) >= 3: return path
        return []


# a fibonacci is determined by the first two elements
# so traverse all possible first two elements means traverse all possibility