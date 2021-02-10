def count_and_say(n: int) -> str:
    if n == 1:
        return '1'
    else:
        s = count_and_say(n-1)
        count = 0
        current_num = ''
        output = ''
        for index, num in enumerate(s):
            if index == 0:
                count += 1
                current_num = str(count) + s[index]

            else:
                if num == s[index - 1]:
                    count += 1
                    current_num = str(count) + s[index]
                else:
                    output += current_num
                    count = 1
                    current_num = str(count) + s[index]
        output += current_num

        return output

print(count_and_say(7))


