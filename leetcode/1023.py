class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = [False] * len(queries)
    
        for i in range(len(queries)):
            pattern_ptr, query_ptr = 0 , 0
            while query_ptr <= len(queries[i]):
                if pattern_ptr == len(pattern):
                    if query_ptr == len(queries[i]):
                        ans[i] = True
                        query_ptr += 1
                    elif queries[i][query_ptr] >= 'A' and queries[i][query_ptr] <= 'Z':
                        break
                    else:
                        query_ptr += 1
                elif query_ptr == len(queries[i]):
                    query_ptr += 1
                elif queries[i][query_ptr] >= 'A' and queries[i][query_ptr] <= 'Z':
                    if queries[i][query_ptr] != pattern[pattern_ptr]:
                        break
                    else:
                        query_ptr += 1
                        pattern_ptr += 1               
                elif queries[i][query_ptr] >= 'a' and queries[i][query_ptr] <= 'z':
                    if queries[i][query_ptr] == pattern[pattern_ptr]:
                        query_ptr += 1
                        pattern_ptr += 1
                    else:
                        query_ptr += 1   
        
        return ans

# 可以尝试正则表达式


