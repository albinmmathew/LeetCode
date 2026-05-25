# Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        if numRows<1:
            return []
        else:    
            while len(ans)<numRows:
                a=[1]
                for i in range(1,len(ans[-1])):
                    a.append(ans[-1][i-1]+ans[-1][i])
                a.append(1)
                ans.append(a)
        return ans