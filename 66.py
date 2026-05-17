# Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result=''.join(map(str,digits))
        num=int(result)
        num+=1
        return list(map(int,str(num)))     