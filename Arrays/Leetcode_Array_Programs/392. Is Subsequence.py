class Solution:
    def isSubsequence(self, c: str, n: str) -> bool:
        if c == n:
            return True
        s = []
        j = 0
        for i in range(len(n)):
            if j < len(c) and c[j] == n[i]:
                s.append(n[i])
                j += 1
            if j == len(c):  
                return True
        return False
        