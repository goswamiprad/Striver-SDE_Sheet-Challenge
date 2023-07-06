class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        attend = [0 for _ in range(len(nums))]

        for num in nums:
            if attend[num]:
                return num
            else:
                attend[num] = 1
        
