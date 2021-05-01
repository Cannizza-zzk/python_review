class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        for i in range(0,len(citations)):
            rest_num =  len(citations) - i
            if rest_num > citations[i]:
                h_index = citations[i]
            elif rest_num == citations[i]:
                return rest_num
            else:
                h_index = rest_num if rest_num > h_index else h_index
                return h_index
        return h_index