class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 각 숫자가 들어갈 딕셔너리를 생성
        major = {}
        for n in nums:
            # 숫자가 major에 있다면
            if major.get(n):
                # 숫자의 갯수를 +1 하고
                major[n] += 1
            else:
                # 숫자가 없으면 1개 있다고 생성한다.
                major[n] = 1
        
        # major 딕셔너리 중 가장 큰 Key를 반환
        return max(major, key=major.get)