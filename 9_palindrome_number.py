class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_og = x
        reversed = 0
        for _ in range(len(str(x))):
            reversed = (reversed * 10) + x % 10
            x = round(x / 10)

            # print(reversed)
        return reversed == x_og

s = Solution()
print(s.is_palindrome(0))