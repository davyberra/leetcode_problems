class Solution:
    def sort(self, nums: list):
        # dict = {
        #     0: 0,
        #     1: 0,
        #     2: 0
        # }
        #
        # for val in nums:
        #     dict[val] += 1
        #
        # output = []
        # for key in dict:
        #     for _ in range(dict[key]):
        #         output.append(key)
        #
        # return output
        pointer = 0
        for _ in range(len(nums)):
            if nums[pointer] == 0:
                temp = nums.pop(pointer)
                nums.insert(0, temp)
                pointer += 1
            elif nums[pointer] == 2:
                temp = nums.pop(pointer)
                nums.append(temp)
            else:
                pointer += 1


s = Solution()
print(s.sort([2,0,2,1,1,0]))
print(s.sort([1]))
