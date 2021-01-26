class Solution:
    def longest_palindrome(self, s: str) -> str:
        output = ''
        if len(s) == 1:
            output = s
        elif len(s) == 2:
            if s[0] == s[1]:
                output = s
            else:
                output = None
        for i, letter in enumerate(s):
            x = 1
            if s[i - x] == s[i + x] and 0 <= i - x < len(s):
                center = letter
                current_palindrome = s[i - x:i + x]
                is_palindrome = True
                x += 1
                while is_palindrome:
                    if s[i - x] != s[i + x] and 0 <= i - x < len(s):
                        if len(current_palindrome) > len(output):
                            output = current_palindrome
                        is_palindrome = False
                    elif s[i - x] == s[i + x] and 0 <= i - x < len(s):
                        current_palindrome = s[i-x:i + x]
                        x += 1

        return output

s = Solution()
print(s.longest_palindrome("badababa"))