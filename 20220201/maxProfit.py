def maxProfit(prices: list[int]) -> int:
    buyday = 0
    sellday = 0
    result = 0
    while sellday < len(prices):
        if prices[sellday] < prices[buyday]:
            buyday = sellday
        else:
            result = max(result, prices[sellday] - prices[buyday])
        sellday += 1
    return result