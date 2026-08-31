class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anas = {}

        for x in strs:

            o = sorted(x)
            ordered = ""
            for i in o:
                ordered += i

            if ordered in anas:
                anas[ordered].append(x)
            else:
                anas[ordered] = [x]
        
        ans = []

        for i in anas:
            ans.append(anas[i])
        return ans