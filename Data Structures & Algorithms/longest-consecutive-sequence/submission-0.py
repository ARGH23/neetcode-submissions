class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxilen = 0

        for i in nums:
            if i-1 not in nums:
                l = 1
                while i+1 in nums:
                    l += 1
                    i += 1
                if l > maxilen:
                    maxilen = l
        
        return maxilen

