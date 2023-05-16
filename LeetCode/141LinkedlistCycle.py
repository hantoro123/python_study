# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 들어올 node를 집합으로 만들고
        node = set()

        # head가 None값이 나올때 까지 반복
        while head:
            # head를 반복중에 node 집합에 포함되면
            if head in node:
                # cycle이 있으므로 true반환
                return True
            # node집합에 없으면 add해주고
            node.add(head)
            # head를 다음 link로 넘어간다.
            head = head.next
        # None값이 나오면 cycle이 없으므로 false반환
        return False
        