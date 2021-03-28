# class Solution:
#     def generateParenthesis(self, n: int) -> list:
#         if n == 1:
#             return ['()']
#         else:
#             output = ['(']
#             for i in range(n - 1):
#
#                 output.append(output[i] + '()')
#                 output[i] += ')('
#         for i in range(len(output)):
#             output[i] += ')'
#         return output


class Solution:
    def generateParenthesis(self, n: int) -> list:
        dict = {
            '(': 1,
            ')': -1
        }
        if n == 1:
            return ['()']
        else:



s = Solution()
print(s.generateParenthesis(2))