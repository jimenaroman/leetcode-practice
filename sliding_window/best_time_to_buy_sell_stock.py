class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # sell > buy day always
        maxProfit = 0
        l = 0
        r = l + 1
        #want the smallest left value, largest right value
        while r < len(prices) :
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                ##only worth updating when actually + val
                maxProfit = max(maxProfit, profit) 
            else: 
                l = r
            r += 1

        return maxProfit
    
"""
Problem:
Best Time to Buy and Sell Stock

Pattern:
Sliding window / two pointers moving forward.

Why not start left at 0 and right at the end:
This is not a two-ends problem. Time order matters, so the sell pointer
should move forward day by day.

Time complexity:
O(n), because right moves through the list once.

Space complexity:
O(1), because only two pointers and max_profit are used.

Pattern trigger:
Need the best difference where the smaller value must come before the
larger value.

The left pointer tracks the best buy day so far.
The right pointer checks each possible sell day.
"""