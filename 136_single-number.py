class Solution:
    def singleNumber(self, nums: list) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


s = Solution()
print(s.singleNumber([4,2,1,2,1]))