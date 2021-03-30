class Solution:
    def maxSubArray(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            high_sum = None
            for i1, val1 in enumerate(nums):
                if nums[i1 - 1] < 0 or i1 == 0:
                    cur_sum = 0
                    for i2, val2 in enumerate(nums[i1:]):
                        cur_sum += val2
                        if high_sum is None:
                            high_sum = cur_sum
                        elif cur_sum > high_sum:
                            high_sum = cur_sum

            return high_sum


nums1 = [1,2,3,-20,4]
nums2 = [-2,1,-3,4,-1,2,1,-5,4]
nums3 = [1]
nums4 = [-1,0,-2]
s = Solution()
print(s.maxSubArray(nums4))

