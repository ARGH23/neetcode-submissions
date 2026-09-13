def solve(make, already):
    #print(make, already)
    #print()
    if len(make) == 0:
        return [already]
    
    else:
        without = solve(make[1:], already)
        within = solve(make[1:], already + [make[0]])
        #print(without)
        #print(within)
        final = without + within
        return final

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return solve(nums, [])
        