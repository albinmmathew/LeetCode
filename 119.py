# Pascal's Triangle II

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex<0:
            return []
        else:
            ans=[[1]]
            while len(ans)<=rowIndex:
                a=[1]
                for i in range(1,len(ans[-1])):
                    a.append(ans[-1][i-1]+ans[-1][i])
                a.append(1)
                ans.append(a)
            return ans[rowIndex]