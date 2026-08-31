class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        lettert = {}

        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
        
        for char in t:
            if char in lettert:
                lettert[char] += 1
            else:
                lettert[char] = 1
        
        for char in s:
            if char not in lettert or lettert[char] != letters[char]:
                return False
        
        for char in t:
            if char not in letters or lettert[char] != letters[char]:
                return False
        
        return True