class Solution:
    def permute(self, nums: list) -> list:
        length = len(nums)
        if length == 1:
            return [[nums[0]]]
        else:
            new_list = self.permute(nums[:length - 1])
            new_nums = []
            for p in new_list:
                count = 0
                while count <= length - 1:
                    new_p = p[:]
                    new_p.insert(count, nums[length - 1])
                    new_nums.append(new_p)
                    count += 1
            return new_nums

s = Solution()
nums = [0,1,2,3,4,5]
print(s.permute(nums))