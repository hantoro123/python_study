class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # merge할 리스트
        merge_list = []
        # 각 리스트가 진행될 인덱스를 표현
        i = j = 0
        # i나 j가 리스트 길이를 넘어가면 종료
        while i < m and j < n:
            # 리스트의 적은 부분을 merge_list에 넣고 인덱스를 +1
            if nums1[i] <= nums2[j]:
                merge_list.append(nums1[i])
                i += 1
            else:
                merge_list.append(nums2[j])
                j+= 1

        # 반복이 끝나면 남은 리스트의 남은 부분을 더해준다. 
        merge_list += (nums1[i:] if i!=m else nums2[j:])
        # nums1을 merge_list로 바꾼다.
        for i in range(m+n):
            nums1[i] = merge_list[i]