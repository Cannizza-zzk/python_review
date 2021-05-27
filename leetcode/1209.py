class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        l_ptr ,  r_ptr = -1 , 1
        dp = [0] * len(s)
        dp[0] = 1
        remove_rcd = {}
        while r_ptr < len(s):
            #print(l_ptr,r_ptr)
            #print(dp)
            if s[r_ptr] == s[r_ptr - 1] and dp[r_ptr - 1] < k:
                dp[r_ptr] = dp[r_ptr - 1] + 1
                r_ptr += 1
            elif s[r_ptr] == s[r_ptr - 1] and dp[r_ptr - 1] == k:
                dp[r_ptr] = 1
                r_ptr += 1
            elif s[r_ptr] != s[r_ptr - 1] and dp[r_ptr - 1] < k:
                dp[r_ptr] = 1
                l_ptr = r_ptr - 1
                r_ptr += 1
            elif s[r_ptr] != s[r_ptr - 1] and dp[r_ptr - 1] == k:
                if l_ptr >= 0 and s[l_ptr] == s[r_ptr]:
                    dp[r_ptr] = dp[l_ptr] + 1
                    back_rcd = {}
                    back_rcd[s[r_ptr]] = dp[r_ptr] - 1
                    while l_ptr >= 0:
                        if dp[l_ptr] != k and s[l_ptr] not in back_rcd:
                            break
                        elif dp[l_ptr] == k and s[l_ptr] not in back_rcd:
                            back_rcd[s[l_ptr]] = 1
                        elif dp[l_ptr] == k and s[l_ptr] in back_rcd:
                            back_rcd[s[l_ptr]] += 1
                        elif s[l_ptr] in back_rcd and dp[l_ptr] == 1:
                            back_rcd[s[l_ptr]] -= 1
                            if back_rcd[s[l_ptr]] == 0:
                                del back_rcd[s[l_ptr]]
                        l_ptr -= 1
                       
                else:
                    dp[r_ptr] = 1
                r_ptr += 1
        ans = []
        #print(dp[487])
        #print(s[487],s[488])
        #print(dp[:248])
        #print(dp[248:])
        for i in range(len(s) - 1, -1, -1):
            if dp[i] != k and s[i] not in remove_rcd:
                ans.append(s[i])
            elif dp[i] == k and s[i] not in remove_rcd:
                remove_rcd[s[i]] = 1
            elif dp[i] == k and s[i] in remove_rcd:
                remove_rcd[s[i]] += 1
            elif s[i] in remove_rcd and dp[i] == 1:
                remove_rcd[s[i]] -= 1
                if remove_rcd[s[i]] == 0:
                    del remove_rcd[s[i]]
        ans.reverse()
        return ''.join(ans)

# better solution ： https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/discuss/392933/JavaC%2B%2BPython-Two-Pointers-and-Stack-Solution
# using stack

                

                

