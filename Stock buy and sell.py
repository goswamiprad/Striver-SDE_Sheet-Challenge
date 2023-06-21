class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max = 0
        max_far = 0
        
        for i in range(1,len(prices)):
            cur_max += prices[i]-prices[i-1]
            if cur_max<0:
                cur_max = 0
            if cur_max>max_far:
                max_far = cur_max
        
        return max_far
