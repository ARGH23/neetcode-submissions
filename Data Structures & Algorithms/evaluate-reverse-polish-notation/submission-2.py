class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            else:
                rt = stack[-1]
                stack.pop()
                lt = stack[-1]
                stack.pop() 

                if i == '+':
                    lt = lt + rt
                    rt = None
                elif i == '-':
                    lt = lt - rt
                    rt = None
                elif i == '*':
                    lt = lt * rt
                else:
                    lt = int(lt / rt)
                stack.append(lt)
        
        return stack[-1]
