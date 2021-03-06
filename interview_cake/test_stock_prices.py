# 1. We can't sell before we buy
# 2. We can't sell right after buying
# 3. We need at least 2 data points

def get_max_profit(stock_prices):
    buy = stock_prices[0]
    sell = stock_prices[1]

    max_profit = sell - buy

    for price in stock_prices[1:]:
        if price < buy:
            buy = price
            continue

        max_profit = max(max_profit, price - buy)

    return max_profit


assert get_max_profit([1, 5, 3, 2]) == 4
assert get_max_profit([7, 2, 8, 9]) == 7
assert get_max_profit([1, 6, 7, 9]) == 8
assert get_max_profit([9, 7, 4, 1]) == -2
assert get_max_profit([1, 1, 1, 1]) == 0

# Tests


# class Test(unittest.TestCase):
#
#     def test_price_goes_up_then_down(self):
#         actual = get_max_profit([1, 5, 3, 2])
#         expected = 4
#         self.assertEqual(actual, expected)
#
#     def test_price_goes_down_then_up(self):
#         actual = get_max_profit([7, 2, 8, 9])
#         expected = 7
#         self.assertEqual(actual, expected)
#
#     def test_price_goes_up_all_day(self):
#         actual = get_max_profit([1, 6, 7, 9])
#         expected = 8
#         self.assertEqual(actual, expected)
#
#     def test_price_goes_down_all_day(self):
#         actual = get_max_profit([9, 7, 4, 1])
#         expected = -2
#         self.assertEqual(actual, expected)
#
#     def test_price_stays_the_same_all_day(self):
#         actual = get_max_profit([1, 1, 1, 1])
#         expected = 0
#         self.assertEqual(actual, expected)
#
#     def test_error_with_empty_prices(self):
#         with self.assertRaises(Exception):
#             get_max_profit([])
#
#     def test_error_with_one_price(self):
#         with self.assertRaises(Exception):
#             get_max_profit([1])
