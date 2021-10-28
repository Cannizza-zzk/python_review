class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid_set = set([0, 1, 8, 2, 5, 6, 9])
        invalid_set = set([0, 1, 8])

        def is_good(x):
            x_digit = set([int(i) for i in str(x)])

            return x_digit.issubset(valid_set) and not x_digit.issubset(invalid_set)

        cnt = 0
        for i in range(1, n+1):
            if is_good(i):
                cnt += 1

        return cnt

# reference: https://leetcode.com/problems/rotated-digits/discuss/116530/JavaPython-O(logN)-Time-O(1)-Space
# lee215 yyds