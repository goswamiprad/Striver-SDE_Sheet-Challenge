class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Bubble Sort
        '''
        flag = True
        while flag:
            ind = 0
            flag = False
            while ind<len(nums)-1:
                if nums[ind+1]<nums[ind]:
                    nums[ind],nums[ind+1] = nums[ind+1],nums[ind]
                    flag = True
                
                ind += 1
        
        '''

        #Easy approach
        zeros = []
        ones = []
        twos = []

        for i in nums:
            if i==0:
                zeros.append(i)
            elif i==1:
                ones.append(i)
            else:
                twos.append(i)
        
        nums[:] = zeros+ones+twos
