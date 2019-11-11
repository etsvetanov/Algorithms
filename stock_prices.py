stock_prices = [40, 15, 20, 6, 10, 7, 5, 8, 11, 21, 9, 1]
# stock_prices = [20, 19, 15, 10]


# complexity is O(n^2) ?
def get_max_profit2(prices):
    max_profit = prices[1] - prices[0]

    if len(prices) == 2:
        return max_profit

    buy_in_price = prices[0]

    for price in prices[2:]:
        profit = price - buy_in_price
        max_profit = max(profit, max_profit)

    return max(max_profit, get_max_profit(prices[1:]))


# complexity is O(n)
def get_max_profit(prices):
    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for price in prices[1:]:
        print('profit', max_profit)
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit()


print(get_max_profit(stock_prices))
assert (get_max_profit(stock_prices) == 16)
