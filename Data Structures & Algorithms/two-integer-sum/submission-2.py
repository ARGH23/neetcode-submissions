class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        vals = {}

        for ind in range(len(nums)):
            i = nums[ind]

            if target-i in vals:
                return [vals[target-i], ind]
            
            vals[i] = ind