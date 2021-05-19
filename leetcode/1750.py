class Solution:
    def minimumLength(self, s: str) -> int:
        p_ptr, b_ptr = 0, len(s) - 1
        while p_ptr != b_ptr:
            targ = ''
            if s[p_ptr] == s[b_ptr]:
                targ = s[p_ptr]
            else:
                break
            while targ == s[p_ptr]:
                p_ptr += 1
            while targ == s[b_ptr]:
                b_ptr -= 1
        
        return b_ptr - p_ptr + 1
