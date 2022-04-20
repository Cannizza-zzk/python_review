class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decode_len, ptr = 0, 0

        for idx, ch in enumerate(s):
            decode_len = decode_len * int(ch) if ch.isdigit() else decode_len + 1
            ptr = idx
            if decode_len >= k: break
        for i in range(ptr,-1,-1):
            if s[i].isdigit():
                decode_len /= int(s[i])
                k %= decode_len
            else:
                if k == decode_len or k == 0:
                    return s[i]
                decode_len -= 1
            



# reference : https://leetcode.com/problems/decoded-string-at-index/discuss/156747/JavaC%2B%2BPython-O(N)-Time-O(1)-Space
# MLE
""" class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decode_list, decode_str = [] , ''
        decode_len = 0
        for ch in s:
            if '2' <= ch <= '9':
                rep = int(ch)
                decode_len *= rep
                if decode_len > k:
                    decode_len /= rep
                    break
            else:
                decode_len += 1
                if decode_len == k:
                    return ch
        k = int(k % decode_len)
        k = decode_len if k == 0 else k
        k = int(k)
        for idx, ch in enumerate(s):
            if '2' <= ch <= '9':
                rep = int(ch)
                decode_str = decode_str * rep
                decode_list = list(decode_str)
            else:
                decode_list.append(ch)
                decode_str = ''.join(decode_list)
            if len(decode_list) >= k:
                    return decode_list[k-1]
                     """