class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #rob current + max(+2) or max(+1)

        maxi = [0] * len(nums)

        maxi[-1] = nums[-1]
        maxi[-2] = max(nums[-2], nums[-1])

        for i in range(-3, -len(nums)-1, -1):
            maxi[i] = max(nums[i] + maxi[i+2], maxi[i+1])
        
        return max(maxi[0], maxi[1])