class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        maxi = 1
        noz = 1
        zc = 0

        for i in nums:
            maxi = maxi * i
            if i == 0:
                zc += 1
            else:
                noz = noz * i
        
        if zc > 1:
            return [0] * len(nums)
        
        ans = []


        for x in nums:
            if x == 0:
                ans.append(int(noz))
            else:
                ans.append(int(maxi/x))
        
        return ans
                