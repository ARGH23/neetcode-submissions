class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        al = len(s1)

        clen = 0

        counts = {}

        for i in s1:
            counts[i] = counts.get(i, 0) + 1


        seen = {}

        for ind in range(len(s2)):
            x = s2[ind]

            if x not in counts:
                clen = 0
                seen = {}
            
            elif x not in seen or seen[x] < counts[x]:
                seen[x] = seen.get(x, 0) + 1
                clen += 1
            
            else:
                minind = ind - clen
                while s2[minind] != x:
                    clen -= 1
                    seen[s2[minind]] -= 1
                    minind += 1


            
            if clen == al:
                return True
            
        
        return False

