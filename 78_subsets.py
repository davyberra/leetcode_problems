class Solution:
    def subsets(self, nums: list) -> list:
        output = []
        for val in nums:
            new_output = output[:]
            new_output.append([val])
            if len(output) > 0:
                for num_set in output:
                    new_set = num_set + [val]
                    new_output.append(new_set)
            output = new_output[:]

        output.append([])
        return output

s = Solution()
print(s.subsets([1,2,3,4]))