# Find Center of Star Graph

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        s=[]
        for e in edges:
            if e[0] in s:
                return e[0]
            s.append(e[0])
            if e[1] in s:
                return e[1]
            s.append(e[1])