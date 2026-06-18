# Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = s.split()
        return len(st[-1])
        # count=0
        # prev=0
        # for i in s:
        #     if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        #         count+=1
        #     else:
        #         if count != 0:
        #             prev = count
        #             count = 0
        # if count!=0:
        #     return count
        # return prev