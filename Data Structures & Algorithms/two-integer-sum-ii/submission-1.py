class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = 0
        l = len(numbers) - 1

        while True:
            x = numbers[f] + numbers[l]
            if x == target:
                return [f+1, l+1]
            elif x < target:
                f += 1
            else:
                l -= 1
        