class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        if len(nums) == 0:
            return 1
        nums.sort()
        i = 1
        for index, num in enumerate(nums):
            if num < 1:
                pass
            elif num == nums[index - 1] and index != 0:
                pass
            else:
                if num != i:
                    return i
                i += 1

        return i

nums = [0,2,2,1,1]

s = Solution()
print(s.firstMissingPositive(nums))
print(1 % 5)