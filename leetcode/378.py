class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ptr_list = [0 for _ in range(len(matrix))]
        for i in range(k):
            ithSamll = float('inf')
            ptr_idx = 0
            for idx , ptr in enumerate(ptr_list):
                if ptr == len(matrix[0]):
                    continue
                if matrix[idx][ptr] < ithSamll:
                    ithSamll = matrix[idx][ptr]
                    ptr_idx = idx
            ptr_list[ptr_idx] += 1
        
        return ithSamll

# like merge sort  
# ignore the information that columns are sorted too faster than 5.02% python3            
