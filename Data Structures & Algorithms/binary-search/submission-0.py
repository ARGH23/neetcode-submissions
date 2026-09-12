class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        mini = 0
        last = len(nums) - 1


        while mini <= last:
            mid = int((mini + last)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                last = mid - 1
            else:
                mini = mid + 1
        
        return -1