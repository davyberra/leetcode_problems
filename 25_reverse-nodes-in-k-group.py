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


def print_head(head):
    if head.next:
        print_head(head.next)

    print(head.val)


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        node = head
        l = []
        done = False
        changed_head = False
        pre_node = None
        new_head = head
        while not done:
            for i in range(k + 1):
                l.append(node)
                if len(l) == k:
                    l.reverse()
                if node.next:
                    node = node.next
                else:
                    break
            if len(l) < k:
                if pre_node:
                    pre_node.next = l[0]
                done = True
            elif len(l) == k:
                if pre_node:
                    pre_node.next = l[0]
                for i in range(k - 1):
                    l[i].next = l[i + 1]
                if not changed_head:
                    new_head = l[0]
                    changed_head = True
                l[-1].next = None
                done = True
            else:
                if pre_node:
                    pre_node.next = l[0]
                for i in range(k):
                    l[i].next = l[i + 1]
                if not changed_head:
                    new_head = l[0]
                    changed_head = True
                node = l[-1]
                pre_node = l[k - 1]
                l = []


        return new_head



head1 = linked_list([1,2,3,4,5,6,7,8,9])
head2 = linked_list([1,2])
s = Solution()
new_head1 = s.reverseKGroup(head2, 2)
print_head(new_head1)