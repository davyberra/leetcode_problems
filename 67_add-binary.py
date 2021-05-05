class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = a, "0" * (len(a) - len(b)) + b
        else:
            a, b = "0" * (len(b) - len(a)) + a, b

        carry, res = "0", ""
        for i in range(len(a) - 1, -1, -1):
            if a[i] == "0" and b[i] == "1" or a[i] == "1" and b[i] == "0":
                if carry == "1":
                    res += "0"
                    carry == "0"
                else:
                    res += "1"
            elif a[i] == '0' and b[i] == '0':
                if carry == "1":
                    res += "1"
                    carry = "0"
                else:
                    res += "0"
            if a[i] == "1" and b[i] == "1":
                if carry == "1":
                    res += "1"
                else:
                    res += "0"
                    carry = "1"
        if carry == "1":
            res += carry

        res = res[::-1]
        return res

s = Solution()
print(s.addBinary("1010", "1011"))
