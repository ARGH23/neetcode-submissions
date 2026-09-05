class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lefti = 0
        righti = len(s) - 1

        while lefti < righti and righti >= 0 and lefti < len(s):
            if (not s[lefti].isalnum()):
                lefti += 1
            elif (not s[righti].isalnum()):
                righti -= 1
            elif (s[lefti].lower() != s[righti].lower()):
                return False
            else:
                lefti += 1
                righti -= 1
        
        return True