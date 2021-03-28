class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return l1
        elif not l1:
            return l2
        elif not l2:
            return l1
        p1, p2 = l1, l2
        head = ListNode()
        if p1.val <= p2.val:
            head.val = p1.val
            p1 = p1.next
        else:
            head.val = p2.val
            p2 = p2.next
        new_node = head
        done = False
        while not done:
            if p1 is None and p2 is None:
                done = True
            elif p1 is None:
                new_node.next = ListNode(val=p2.val)
                p2 = p2.next
            elif p2 is None:
                new_node.next = ListNode(val=p1.val)
                p1 = p1.next
            else:
                if p1.val <= p2.val or p2 is None:
                    new_node.next = ListNode(val=p1.val)
                    p1 = p1.next
                else:
                    new_node.next = ListNode(val=p2.val)
                    p2 = p2.next
            new_node = new_node.next

        return head


def linked_list(nums: list) -> ListNode:
    head = ListNode(val=nums[0])
    new_node = head
    for value in nums[1:]:
        new_node.next = ListNode(val=value)
        new_node = new_node.next

    return head

head1 = linked_list([1,2,4])
head2 = linked_list([1,3,4])

s = Solution()
merged_head = s.mergeTwoLists(head1, head2)

def print_head(head):
    if head.next:
        print_head(head.next)

    print(head.val)

print_head(merged_head)
