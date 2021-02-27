class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        nums.sort()
        output = []
        for i, value in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if target - sum > nums[r]:
                    r -= 1
                if target - sum < nums[l]:
                    l += 1
                else:
                    if target

s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))
print(s.fourSum([-1,-5,-6,-2,1,7,3,4,-5,-3,8,9,0,0,-2], 1))
