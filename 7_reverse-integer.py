class Solution:
    def reverse(self, x: int) -> int:
        num_list = list(str(x))
        num_list.reverse()
        num_string = ''
        for num in num_list:
            num_string += num
        output = int(num_string)
        return output

s = Solution()
print(s.reverse(123456789))