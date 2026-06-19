# Excel Sheet Column Title

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        soln=""
        while columnNumber:
            columnNumber-=1
            soln=chr(columnNumber%26+ord('A'))+soln
            columnNumber//=26
        return soln