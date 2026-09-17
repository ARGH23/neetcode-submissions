class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # s1[i:], s2[j:] = max(s1[i+1:]s2[j:], s1[i:]s2[j+1:], 1 + s1[i+1:]s2[j+1] if match)

        i = len(text1)
        j = len(text2)


        palinlen = []

        for _ in range(i):
            toadd = []
            for _ in range(j):
                toadd.append(0)
            palinlen.append(toadd)

        if text1[i-1] == text2[j-1]:
            palinlen[i-1][j-1] = 1
        
        for oi in range(i-1, -1, -1):
            for ti in range(j-1, -1, -1):

                pm = palinlen[oi][ti]

                if oi + 1 < i:
                    pm = max(pm, palinlen[oi+1][ti])
                if ti + 1 < j:
                    pm = max(pm, palinlen[oi][ti+1])
                if text1[oi] == text2[ti]:
                    if oi + 1 < i and ti + 1 < j:
                        pm = max(pm, 1+palinlen[oi+1][ti+1])
                    else:
                        pm = max(pm, 1)

                palinlen[oi][ti] = pm

        #print(palinlen)
        return palinlen[0][0]

