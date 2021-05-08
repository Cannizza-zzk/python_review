class Solution:
    def countOfAtoms(self, formula: str) -> str:
        times_stack = []
        elements_now = ''
        ansRcd = {}
        while len(formula) != 0:
            char_now = formula[-1]
            formula = formula[:-1]
            if char_now >= 'a' and char_now <= 'z': #lower case
                if elements_now != '' and elements_now[0] >= '0' and elements_now[0] <= '9':
                    times_stack.append(int(elements_now))
                    elements_now = ''
                elif elements_now == '':
                    times_stack.append(1)
                elements_now = char_now + elements_now
            elif char_now >= 'A' and char_now <= 'Z': #upper case
                if elements_now != '' and elements_now[0] >= '0' and elements_now[0] <= '9':
                    times_stack.append(int(elements_now))
                    elements_now = ''
                elif elements_now == '':
                    times_stack.append(1)
                elements_now = char_now + elements_now
                
                times = 1
                for i in times_stack:
                        times *= i
                if ansRcd.get(elements_now) == None:
                    ansRcd[elements_now] = times    
                else:
                    ansRcd[elements_now] += times
                times_stack.pop()
                elements_now = ''
            elif char_now >= '0' and char_now <= '9':
                elements_now = char_now + elements_now
            elif char_now == ')':
                if elements_now != '' and elements_now[0] >= '0' and elements_now[0] <= '9':
                    times_stack.append(int(elements_now))
                    elements_now = ''
                elif elements_now == '':
                    times_stack.append(1)
            elif char_now == '(':
                if len(times_stack) != 0:
                    times_stack.pop()


        # output
        ansStringlist = []
        ansString = ''
        for atom,num in ansRcd.items():
            if num != 1:
                ansStringlist.append(atom + str(num))
            else:
                ansStringlist.append(atom)
        for string in sorted(ansStringlist):
            ansString = ansString + string
        return ansString