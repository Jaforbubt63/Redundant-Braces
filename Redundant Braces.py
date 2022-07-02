class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stk = []
        
        for ch in A:
            if ch == ')':
                x = stak.pop()
                if x == '(':
                    return 1
                operator = False
                while x != '(':
                    if x in "+-*%":
                        operator = True
                    x = stk.pop()
                if operator is False:
                    return 1
                continue
            stk.append(ch)
            
        return 0
                    
