class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}

        clen = 0
        maxlen = -1

        ind = 1
        for char in s:
            if char not in seen:
                clen += 1
                seen[char] = ind
            elif ind - clen > seen[char]:
                seen[char] = ind
                clen += 1
            else:
                maxlen = max(maxlen, clen)
                newstart = seen[char] + 1
                clen = ind + 1 - newstart

                seen[char] = ind

            ind += 1
        
        return max(clen, maxlen)
        