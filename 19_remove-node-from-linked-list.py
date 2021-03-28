# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0:
            return head
        else:
            count = 0
            dict = {
                count: head,
            }
            new_node = head.next
            count += 1
            while new_node is not None:
                dict[count] = new_node
                new_node = new_node.next
                count += 1

            if count == n and count == 1:
                return ListNode(val='')
            elif count == n and count != 1:
                head = head.next
                return head
            else:
                dict[count - (n + 1)].next = dict[count - n].next
                return head

nums = [1,2,3,4,5]
h = ListNode(val=nums[0])
new_node = h
for value in nums[1:]:
    new_node.next = ListNode(val=value)
    new_node = new_node.next

s = Solution()
print(s.removeNthFromEnd(head=h, n=1))


