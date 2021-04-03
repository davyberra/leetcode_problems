class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        i = len(nums) // 2
        j, k = 0, len(nums)
        output = [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return output
        while j < k:
            if nums[i] < target:
                j = i + 1
                i = len(nums[j:k]) // 2 + j
            elif nums[i] > target:
                k = i
                i = len(nums[j:k]) // 2 + j
            elif nums[i] == target:
                if i > 0:
                    while nums[i - 1] == target:
                        i -= 1
                        if i < 1:
                            break
                j = i
                if i < len(nums) - 1:
                    while nums[i + 1] == target:
                        i += 1
                        if i > len(nums) - 2:
                            break
                k = i

                output[0], output[1] = j, k
                return output

        return output

nums = [-99999,-99998,-9999,-999,-99,-9,-1]
target = 0

s = Solution()
# print(s.searchRange(nums, target))
# print(nums[0:1])
print(0 // 2)
