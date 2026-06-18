# Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        soln=""
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                soln = soln + strs[0][i]
            else:
                break
        return soln