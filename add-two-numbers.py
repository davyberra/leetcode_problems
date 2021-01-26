
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_str = ''
        l2_str = ''
        for i in l1:
            l1_str = l1_str + l1[i]
        for i in l2:
            l2_str = l2_str + l2[i]
        l1_int, l2_int = int(l1_str), int(l2_str)
        sum_int = l1_int + l2_int
        sum_str = str(sum_int)
        sum_list = []
        for i in sum_str:
            sum_list.append(sum_str[i])

        return sum_list


