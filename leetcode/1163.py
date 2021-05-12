class Solution:
    def max_lexorder(self,s1:str,s2:str):
        if len(s1)>len(s2):
            if s1[:len(s2)] == s2:
                return False
            else:
                for i in range(len(s2)):
                    if s1[i] < s2[i]:
                        return True
                    elif s1[i] > s2[i]:
                        return False
                    else:
                        continue
        else:
            if s2[:len(s1)] == s1:
                return False
            else:
                for i in range(len(s1)):
                    if s1[i] < s2[i]:
                        return True
                    elif s1[i] > s2[i]:
                        return False
                    else:
                        continue

    def lastSubstring(self, s: str) -> str:
        if len(s) == 0:
            return ''
        ans_str = s[0]
        for i in range(1,len(s)):
            if s[i] > ans_str[0]:
                ans_str = s[i]
            elif s[i] < ans_str[0]:
                ans_str += s[i]
            else:
                flag = self.max_lexorder(ans_str,s[i:])
                if flag:
                    ans_str = s[i]
                else:
                    ans_str += s[i]
        return ans_str