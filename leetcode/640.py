class Solution:
    def solveEquation(self, equation: str) -> str:
        l_numx , r_numx = 0 , 0
        l_sum , r_sum = 0 , 0
        operation = ['+' , '-' , '=']
        operand , np = 0 , 1
        left = True
        for idx,char in enumerate(equation):
            if char in operation:
                if char == '=':
                    l_sum += np * operand
                    np = 1
                    left = False
                elif char == '-':
                    if left: 
                        l_sum += np * operand
                    else:
                        r_sum += np * operand
                    np = -1
                elif char == '+':
                    if left: 
                        l_sum += np * operand
                    else:
                        r_sum += np * operand
                    np = 1
                operand = 0
            else:
                if char == 'x':
                    if left:
                        l_numx += np*operand if idx >0 and equation[idx - 1] not in operation else np
                    else:
                        r_numx += np*operand if idx >0 and equation[idx - 1] not in operation else np
                    operand = 0
                else:
                    operand = 10 * operand + int(char)
        
        if operand != 0:
            r_sum += operand * np

        if r_sum == l_sum and r_numx == l_numx:
            return 'Infinite solutions'
        elif r_sum == l_sum and r_numx != l_numx:
            return 'x=0'
        elif r_sum != l_sum and r_numx == l_numx:
            return 'No solution'
        else:
            ans = (r_sum - l_sum) / (l_numx - r_numx)
            return 'x='+str(int(ans))

        


