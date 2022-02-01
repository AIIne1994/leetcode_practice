def maxProfit(prices: list[int]) -> int:
    buyprice = prices[0]
    profits = [0]
    for day, price in enumerate(prices):
        if price < buyprice:
            buyprice = price
        profits.append(price - buyprice)

    return max(profits)
