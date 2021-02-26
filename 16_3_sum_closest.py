class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        output = None
        for i in range(len(nums) -2):
            l, r = i + 1, len(nums) - 1
            current_sum = None
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum == target:
                    return current_sum
                elif current_sum > target:
                    r -= 1
                elif current_sum < target:
                    l += 1
                if output is None or abs(output - target) > abs(current_sum - target):
                    output = current_sum

        return output


s = Solution()
print(s.threeSumClosest([1,2,5,10,11], 12))
