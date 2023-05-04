class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # ListNode class형의 merge_list와 temp 생성
        merge_list = temp = ListNode()
        # list1이나 list2가 끝날때 까지 실행하며
        while list1 and list2:
            # list1의 val이 list2의 val보다 크다면
            if list1.val > list2.val:
                # temp의 next가 list2이고
                temp.next = list2
                # list2가 list2의 next로 temp가 list2로 이동
                list2, temp = list2.next, list2
            else:
                # 반대라면 temp의 next에 list1을 넣고
                temp.next = list1
                # list1이 list1의 next로 temp가 list1로 이동
                list1, temp = list1.next, list1
            
        # list1과 list2중에 남아있는게 있으면
        if list1 or list2:
            #temp에 next에 이어 붙이는데
            # 이 문법은 list1이 참이면 list1 아니면 list2를 붙이는 것이다.
            temp.next = list1 if list1 else list2

        # 최종적으로 merge_list의 next를 출력하면 된다.
        return merge_list.next