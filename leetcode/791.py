class Solution:
    def customSortString(self, order: str, str: str) -> str:
        str_dict = collections.Counter(str)
        ans = ''
        for i in range(len(order)):
            if order[i] in str_dict:
                ans += order[i]*str_dict[order[i]]
                str_dict.pop(order[i])
        
        for char, char_cnt in str_dict.items():
            ans += char*char_cnt
        return ans