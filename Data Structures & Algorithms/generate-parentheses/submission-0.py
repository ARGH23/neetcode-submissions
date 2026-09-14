class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = ['']


        def solve(forward, backward, ans):
            if forward + backward == 0:
                return ans
            
            if forward == 0:
                for i in range(len(ans)):
                    ans[i] = ans[i] + backward * ')'
                return ans
            
            if forward == 1 and backward == 1:
                for i in range(len(ans)):
                    ans[i] = ans[i] + '()'
                return ans

            if forward == backward:
                for i in range(len(ans)):
                    ans[i] = ans[i] + '('
                return solve(forward - 1, backward, ans)

            fw = ans.copy()
            bw = ans.copy()
            fa = []
            for i in range(len(fw)):
                fw[i] = fw[i] + '('
            fa += solve(forward-1,backward, fw)
            for i in range(len(bw)):
                bw[i] = bw[i] + ')'
            fa += solve(forward, backward-1, bw)
            return fa
        
        return solve(n, n, ans)