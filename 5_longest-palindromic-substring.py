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
        else:
            i = 1
            while i < len(s):
                x = 1
                if 0 < i < (len(s) - 1):
                    if s[i - x] == s[i + x]:
                        current_palindrome = s[i - x:i + x + 1]
                        is_palindrome = True
                        x += 1
                        while is_palindrome:
                            if 0 <= (i - x) < (i + x) < len(s):
                                if s[i - x] != s[i + x]:
                                    if len(current_palindrome) > len(output):
                                        output = current_palindrome
                                    is_palindrome = False
                                elif s[i - x] == s[i + x]:
                                    current_palindrome = s[i - x:i + x + 1]
                                    x += 1
                            else:
                                is_palindrome = False
                        if len(current_palindrome) > len(output):
                            output = current_palindrome
                i += 1

        return output

s = Solution()
print(s.longest_palindrome("dxbababdheigieh"))