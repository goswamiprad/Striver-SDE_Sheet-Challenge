class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start,end):
            while start<end:
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end -= 1
            
            return

        n = len(nums)
        
        ind = n-2
        
        while ind>=0:
            if nums[ind]<nums[ind+1]:
                break
            ind -= 1
        
        if ind>=0:
            j = n-1
            while j>ind:
                if nums[j]>nums[ind]:
                    nums[j],nums[ind] = nums[ind],nums[j]
                    break
                j -= 1
        
        reverse(ind+1,n-1)

        return
