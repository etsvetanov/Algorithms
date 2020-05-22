# def test(a, b, c):
#     print(a, b, c)
#
# test('a', 'b', 'c')

# 2 args, vending machine, cost of item, money supplied, return [] with possible coins [1, 2, 5, 10, 20, 50, 100, 200]

COIN_VALUES = [200, 100, 50, 20, 10, 5, 2, 1]

def vendingMachine(payment, cost_of_item):
    change_value = payment - cost_of_item
    change = [0, 0, 0, 0, 0, 0, 0, 0]

    for i, coin_value in enumerate(COIN_VALUES):
        change[i] = change_value // coin_value  # number of coins of given value
        change_value = change_value % coin_value  # remainder

    return list(reversed(change))

# print(vendingMachine(500, 150))

# tests
print(vendingMachine(500, 240))
print(vendingMachine(200, 80))
print(vendingMachine(200, 60))
print(vendingMachine(180, 22))
print(vendingMachine(1000, 10))