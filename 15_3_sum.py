class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        return nums


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4,5,2]))
