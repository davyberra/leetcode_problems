class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        string_to_int = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }
        int_to_string = {
            0: '0',
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
        }
        product_string = ''
        product_array = []
        num1_int, num2_int = 0, 0
        for val in num1:
            num1_int += string_to_int[val]
            num1_int *= 10
        num1_int /= 10
        num1_int = int(num1_int)
        for val in num2:
            num2_int += string_to_int[val]
            num2_int *= 10
        num2_int /= 10
        num2_int = int(num2_int)

        product = num1_int * num2_int
        if product == 0:
            return "0"
        while product > 0:
            product_array.append(int_to_string[product % 10])
            product //= 10

        for i in range(len(product_array) - 1, -1, -1):
            product_string += product_array[i]

        return product_string



num1, num2 = "9333852702227987", "85731737104263"

s = Solution()
print(s.multiply(num1, num2))
