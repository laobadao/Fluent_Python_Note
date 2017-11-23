class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        # self.nodes = []


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


if __name__ == '__main__':
    mul_list = []
    idx = ListNode(6)
    n = idx
    n.next = ListNode(3)
    n = n.next
    n.next = ListNode(5)
    n = n.next

    mul_list.append(idx)

    solu = Solution()
    re = solu.mergeKLists(mul_list)
    print(re.val)
