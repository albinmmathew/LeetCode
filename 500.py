# Keyboard Row

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first="qwertyuiopQWERTYUIOP"
        second="asdfghjklASDFGHJKL"
        third="zxcvbnmZXCVBNM"
        soln=[]
        for word in words:
            include=True
            if word[0] in first:
                for i in word:
                    if i not in first:
                        include=False
                        break
            elif word[0] in second:
                for i in word:
                    if i not in second:
                        include=False
                        break
            else:
                for i in word:
                    if i not in third:
                        include = False
                        break
            if include:
                soln.append(word)
        return soln