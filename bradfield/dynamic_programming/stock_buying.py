class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        buy stock
        look at next values to sell
        find max
        """
        max_profit = 0
        for idx, buy_price in enumerate(prices[:-1]):
            if all(prices[i] >= prices[i + 1] for i in range(len(prices) - 1)):
                return max_profit
            for sell_price in prices[idx + 1:]:
                if sell_price - buy_price > max_profit:
                    max_profit = sell_price - buy_price
        return max_profit

s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]) == 5)
