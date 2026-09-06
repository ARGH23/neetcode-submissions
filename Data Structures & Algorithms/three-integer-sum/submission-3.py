class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        nums = sorted(nums)

        for i in range(len(nums)):
            target = -nums[i]

            smallest = i+1
            largest = len(nums) - 1

            while smallest < largest:
                if nums[smallest] + nums[largest] < target:
                    smallest += 1
                elif nums[smallest] + nums[largest] > target:
                    largest -= 1
                else:
                    pans = [-1*target, nums[smallest], nums[largest]]
                    if pans not in ans:
                        ans.append(pans)
                    smallest += 1
                    largest -= 1
            
            

        return ans
