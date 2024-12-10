class Solution:
    def romanToInt(self, s: str) -> int:
        c = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        n = 0
        i = 0
        while i<len(s):
            if i < len(s)-1 and c[s[i]] < c[s[i+1]]:
                n += c[s[i+1]] - c[s[i]]
                i += 2
            else:
                n += c[s[i]]
                i += 1
        return n