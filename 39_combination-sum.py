class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        candidates.sort()
        while candidates[-1] > target:
            candidates.pop()



        return candidates

candidates = [2,3,5,8,12,13,17,22]
target = 30

s = Solution()
print(s.combinationSum(candidates, target))
