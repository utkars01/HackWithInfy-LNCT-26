class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
    
        for price in prices:
        # Update minimum price
            if price < min_price:
                min_price = price
        
        # Calculate profit
            profit = price - min_price
        
        # Update max profit
            if profit > max_profit:
                max_profit = profit
    
        return max_profit