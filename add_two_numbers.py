# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        l1.reverse()
        l2.reverse()
        l1_str = ''
        l2_str = ''
        for i in range(len(l1)):
            l1_str = l1_str + str(l1[i])
        for i in range(len(l2)):
            l2_str = l2_str + str(l2[i])
        l1_int, l2_int = int(l1_str), int(l2_str)
        sum_int = l1_int + l2_int
        sum_str = str(sum_int)
        sum_list = []
        for i in range(len(sum_str)):
            sum_list.append(int(sum_str[i]))
        sum_list.reverse()

        return sum_list


obj = Solution()
print(obj.addTwoNumbers([1], [2]))
print(obj.addTwoNumbers([1, 2, 3], [1, 2, 3]))
print(obj.addTwoNumbers([4, 1, 5, 8], [1, 6, 3, 8, 2]))
print(8514 + 28361)