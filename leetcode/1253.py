class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if lower + upper != sum(colsum):
            return []

        col_num = len(colsum)
        res = [[0 for _ in range(col_num)] for _ in range(2)]

        for idx , cur_colsum in enumerate(colsum):
            if cur_colsum > 2:
                return []
            elif cur_colsum == 2:
                if upper == 0 or lower == 0:
                    return []
                res[0][idx] += 1
                res[1][idx] += 1
                upper -= 1
                lower -= 1
            elif cur_colsum == 0:
                continue
            else:
                col_idx = 0 if upper >= lower else 1
                res[col_idx][idx] += 1
                if col_idx == 0:
                    upper -= 1
                else:
                    lower -= 1

        return res
