class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor > 0 and dividend > 0 or divisor < 0 and dividend < 0:
            sign = '+'
        else:
            sign = '-'
        dividend, divisor = abs(dividend), abs(divisor)
        remainder = dividend
        quotient = 0
        if divisor == 1:
            quotient = dividend
            remainder = 0
        while remainder >= divisor:
            temp, i = divisor, 1
            while remainder >= temp:
                remainder -= temp
                quotient += i
                i <<= 1
                temp <<= 1


        if sign == '-':
            quotient = -quotient
        quotient = min(quotient, 2147483647)
        quotient = max(-2147483648, quotient)
        return quotient


s = Solution()
print(s.divide(-2147483648, -3))