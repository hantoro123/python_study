class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums에서 비교할 인덱스
        start = 0
        for i in range(1,len(nums)):
            # 비교했을때 같으면 넘어가고
            if nums[start] == nums[i]:
                continue
            else:
                # 다르면 start의 다음 인덱스를 i인덱스 값으로 바꾸고
                nums[start+1] = nums[i]
                # start를 다음 인덱스로
                start += 1

        # start+1인덱스 를 반환해준다.
        return start+1
