class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        maxi = nums[0]
        suminpro = 0
        for i in nums:
            suminpro += i
            if suminpro>maxi:
                maxi = suminpro
            if suminpro<0:
                suminpro = 0
        return maxi
        '''

        '''

        def recur(ind,dp):
            if ind==0:
                return nums[ind]
            
            dp[ind] = max(nums[ind],nums[ind]+recur(ind-1,dp))
            
            return dp[ind]
        
        dp = [-1 for _ in range(len(nums))]
        dp[0] = nums[0]

        recur(len(nums)-1,dp)
        
        return max(dp)

        '''

        summ = 0
        maxi = nums[0]

        for i in nums:
            if i>summ+i:
                summ = i
            else:
                summ += i
            
            maxi = max(maxi,summ)
        
        return maxi
