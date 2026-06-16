# Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        total=0
        for i in range(len(s)):
            if i+1<len(s):
                if s[i] == "C" and (s[i+1] == "M" or s[i+1] == "D"):
                    total-=100
                    continue
                elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                    total-=10
                    continue
                elif s[i] == "I" and (s[i+1] == "X" or s[i+1] == "V"):
                    total-=1
                    continue
            if s[i] == "M":
                total+=1000
            elif s[i] == "C":
                total+=100
            elif s[i] =="D":
                total+=500
            elif s[i] == "X":
                total+=10
            elif s[i] == "L":
                total+=50
            elif s[i] == "I":
                total+=1
            else:
                total+=5
        return total