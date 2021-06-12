import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def recursor(total: int, nums_left: list, n: int, k: int):
            if len(nums_left) == 1:
                next_num = nums_left.pop()
                s_list.append(str(next_num))
                return None
            else:
                for j in range(len(nums_left) - 1, 0, -1):
                    for i in range(len(nums_left)):
                        cur_total = total + (math.factorial(j) * (i + 1))
                        if k <= cur_total:
                            next_num = nums_left.pop(i)
                            s_list.append(str(next_num))
                            recursor(
                                total=total + math.factorial(j) * i,
                                nums_left=nums_left,
                                n=n,
                                k=k
                            )
                            break
        nums = [i for i in range(1, n+1)]
        s_list = []

        recursor(
            total=0,
            nums_left=nums,
            n=n,
            k=k
        )
        s = ''
        for val in s_list:
            s += val

        return s



s = Solution()
print(s.getPermutation(9, 56))
print(5 % 5)