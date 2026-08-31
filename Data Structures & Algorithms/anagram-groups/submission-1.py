class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anas = {}

        for x in strs:

            ordered = tuple(sorted(x))

            if ordered in anas:
                anas[ordered].append(x)
            else:
                anas[ordered] = [x]
        
        ans = []

        for i in anas:
            ans.append(anas[i])
        return ans