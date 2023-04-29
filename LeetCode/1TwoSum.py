class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # start and end for List index
        for start in range(len(nums)-1):
            # end is start + 1 to len(List)-1
            end = start + 1
            while end < len(nums):
                # sum is to same target return start,end index 
                if nums[start] + nums[end] == target:
                    return [start, end]
                else:
                    # not same do end plus 1
                    end += 1
                    