class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        #rob current + max(+2) or max(+1)

        #w/o 0
        maxi = [0] * len(nums)

        maxi[-1] = nums[-1]
        maxi[-2] = max(nums[-2], nums[-1])

        for i in range(-3, -len(nums), -1):
            maxi[i] = max(nums[i] + maxi[i+2], maxi[i+1])
        
        fr =  max(maxi[1], maxi[2])


        #w/o -1
        maxi = [0] * len(nums)

        maxi[-2] = nums[-2]
        maxi[-3] = max(nums[-3], nums[-2])

        for i in range(-4, -len(nums) -1, -1):
            maxi[i] = max(nums[i] + maxi[i+2], maxi[i+1])
        
        sr =  max(maxi[0], maxi[1])

        return max(fr, sr)