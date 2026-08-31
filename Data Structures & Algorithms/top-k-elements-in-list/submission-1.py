class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        buckets = {}

        for x in count:
            if count[x] in buckets:
                buckets[count[x]].append(x)
            else:
                buckets[count[x]] = [x]
        
        ans = []

        for i in range(len(nums), 0, -1):
            if i in buckets:
                ans += buckets[i]
                if len(ans) == k:
                    return ans
        