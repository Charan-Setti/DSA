class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w3 = []
        if len(word1)>len(word2):
            for i in range(len(word2)):
                w3.append(word1[i]+word2[i])
            w3.append(word1[len(word2):])
            
        elif(len(word1)<len(word2)):
            for i in range(len(word1)):
                w3.append(word1[i]+word2[i])
            w3.append(word2[len(word1):])
        
        else:
            for i in range(len(word1)):
                w3.append(word1[i]+word2[i])
        return ''.join(w3)