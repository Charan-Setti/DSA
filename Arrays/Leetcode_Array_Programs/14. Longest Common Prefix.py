class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=''
        flag = True
        y = strs[0]
        for i in strs:
            if len(i)<len(y):
                y = i
        for i in range(len(y)):
            for j in range(len(strs)):
                if strs[0][i] != strs[j][i]:
                    flag = False
                    break
            if flag == True:
                s = s + strs[0][i]
            else:
                break
        return s
        