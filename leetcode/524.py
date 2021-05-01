class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        index_dict = {}
        res = []
        for i in range(0,len(dictionary)):
            index_dict[dictionary[i]] = 0

        for i in range(0,len(s)):
            for dict_string, index in index_dict.items():
                if s[i] == dict_string[index] and index != -1:
                    if index == len(dict_string) - 1:
                        res.append(dict_string)
                        index_dict[dict_string] =  -1
                    else:
                        #print(s[i],dict_string)
                        index_dict[dict_string] += 1
            
        
        ans = sorted(res, key = lambda x : (-len(x),x))
        
        if len(ans) != 0:
            return ans[0]
        else:
            return ''