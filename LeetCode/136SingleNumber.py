class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 들어온 리스트를 정렬하고 single_num에 0번을 넣어준다.
        nums.sort(); single_num = nums[0]
        for i in range(1,len(nums)-1):
            # 만약에 지금 숫자가 -1 or +1 인덱스에 같은 숫자가 있으면
            if nums[i] == nums[i+1] or nums[i] == nums[i-1]:
                # 다음으로
                continue
            else:
                # 앞뒤가 다르면 이번호를 single_num에 넣고 멈춘다.
                single_num = nums[i]
                break

        # 만약에 길이가 2이상이면 마지막 번호도 체크
        if len(nums) > 1 and nums[-1] != nums[-2]:
            single_num=nums[-1]

        # 최종적으로 single_num을 반환한다.
        return single_num
