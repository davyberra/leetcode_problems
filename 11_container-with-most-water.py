class Solution:
    def maxArea(self, height: list) -> int:
        output = 0
        area = 0
        for index1, num1 in enumerate(height):
            for index2, num2 in enumerate(height[index1 + 1:]):
                if num2 >= num1:
                    area = num1 * (index2 + 1)
                else:
                    area = num2 * (index2 + 1)
                if area > output:
                    output = area

        return output


s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))
print(s.maxArea([4,3,2,1,4]))
print(s.maxArea([1,2,1]))