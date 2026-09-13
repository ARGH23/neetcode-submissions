class Solution:
    def trap(self, height: List[int]) -> int:
        left = None
        right = None
        lastdone = 0

        total = 0
        current = 0

        for i in range(len(height)):
            cur = height[i]

            if left == None:
                left = cur

            elif right == None:
                if cur >= left:
                    left = cur
                else:
                    right = cur
                    current += (left - cur)
            
            elif cur < left:
                current += (left - cur)
            else:
                total += current
                current = 0
                left = cur
                right = None
                lastdone = i

        if current > 0:
            current = 0
            left = None
            right = None

            for i in range(len(height)-1, lastdone-1, -1):
                cur = height[i]

                if right == None:
                    right = cur

                elif left == None:
                    if cur >= right:
                        right = cur
                    else:
                        left = cur
                        current += (right - cur)
                
                elif cur < right:
                    current += (right - cur)
                else:
                    total += current
                    current = 0
                    left = None
                    right = cur


        return total
