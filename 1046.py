# Last Stone Weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            s1 = max(stones)
            stones.remove(s1)
            s2 = max(stones)
            stones.remove(s2)
            if s1 == s2:
                continue
            else:
                stones.append(abs(s1-s2))
            # print(stones)
        if stones:
            return stones[0]
        else:
            return 0