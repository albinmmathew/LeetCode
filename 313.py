# Super Ugly Number

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp=[1]
        ugly=1
        index=[0]*len(primes)
        ugly_nums = [1]*len(primes)
        for i in range(1,n):
            for j in range(0,len(primes)):
                if ugly_nums[j]==ugly:
                    ugly_nums[j]=dp[index[j]]*primes[j]
                    index[j]+=1
            ugly = min(ugly_nums)
            dp.append(ugly)       
        return dp[-1]