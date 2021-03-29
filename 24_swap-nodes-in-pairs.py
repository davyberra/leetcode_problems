class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list(nums: list) -> ListNode:
    head = ListNode(val=nums[0])
    new_node = head
    for value in nums[1:]:
        new_node.next = ListNode(val=value)
        new_node = new_node.next

    return head

head1 = linked_list([1,2,3,4,5,6,7,8,9,10])




def print_head(head):
    if head.next:
        print_head(head.next)

    print(head.val)


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def get_pairs(count, head: ListNode):
            if head is None:
                return head

            if count == 0:
                first = head
                if head.next:
                    second = head.next
                    first.next = head.next.next
                    second.next = first
                    count += 1
                    get_pairs(count, first)
                    return second
                else:

                    return first
            else:
                if head.next:
                    first = head.next

                    if head.next.next:
                        second = head.next.next

                        head.next = second
                        first.next = second.next

                        second.next = first

                        count += 2
                        get_pairs(count, first)

        return get_pairs(0, head)




s = Solution()
new_head = s.swapPairs(head1)
print_head(new_head)
# print(new_head.val)

