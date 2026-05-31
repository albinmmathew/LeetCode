# Find the Town Judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        IN = [0]*(n+1)
        OUT = [0]*(n+1)

        for x in trust:
            OUT[x[0]]+=1
            IN[x[1]]+=1
        
        for i in range(1,n+1):
            if (IN[i]==n-1) and (OUT[i]==0):
                return i
        return -1