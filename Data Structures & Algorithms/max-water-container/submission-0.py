class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxa = -1


        while left < right:
            height = min(heights[left], heights[right])
            base = right - left
            area = height*base
            if area > maxa:
                maxa = area
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxa
