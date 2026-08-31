class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        i = 0
        for temp in temperatures:
            if not stack:
                stack.append([temp, i])
            elif temp <= stack[-1][0]:
                stack.append([temp, i])
            else:
                while stack and temp > stack[-1][0]:
                    ans[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                stack.append([temp, i])

            i += 1
        
        return ans
